# Copyright © 2026 Weblate authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import hashlib
import hmac
import re
from datetime import datetime, timezone

from fastapi import (
    Depends,
    FastAPI,
    File,
    Header,
    HTTPException,
    Request,
    UploadFile,
    status,
)
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, ValidationError, field_validator

from weblate_in_context_gateway.config import Settings
from weblate_in_context_gateway.models import BindingManifest, ReviewUnit
from weblate_in_context_gateway.store import ManifestStore
from weblate_in_context_gateway.weblate import WeblateClient


class CommentRequest(BaseModel):
    comment: str = Field(min_length=1, max_length=1000)

    @field_validator("comment")
    @classmethod
    def validate_comment(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Comment must not be empty")
        return value.strip()


def sign_payload(secret: str, payload: bytes) -> str:
    digest = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return f"sha256={digest}"


def create_app(
    settings: Settings,
    *,
    store: ManifestStore | None = None,
    weblate_client: WeblateClient | None = None,
) -> FastAPI:
    manifest_store = store or ManifestStore()
    client = weblate_client or WeblateClient(
        settings.weblate_url, settings.weblate_api_token
    )
    app = FastAPI(title="Weblate in-context review gateway", version="0.1.0")
    if settings.allowed_origins:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=list(settings.allowed_origins),
            allow_credentials=True,
            allow_methods=["GET", "POST"],
            allow_headers=["Authorization", "Content-Type"],
        )

    def require_review_session(authorization: str = Header()) -> None:
        expected = f"Bearer {settings.review_session_token}"
        if not hmac.compare_digest(authorization, expected):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid review session")

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.post("/v1/manifests", status_code=status.HTTP_204_NO_CONTENT)
    async def ingest_manifest(
        request: Request,
        x_weblate_review_signature: str = Header(),
    ) -> None:
        payload = await request.body()
        expected = sign_payload(settings.manifest_secret, payload)
        if not hmac.compare_digest(x_weblate_review_signature, expected):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid signature")
        try:
            manifest = BindingManifest.model_validate_json(payload)
        except ValidationError as error:
            raise HTTPException(
                status.HTTP_422_UNPROCESSABLE_ENTITY, "Invalid manifest"
            ) from error
        if manifest.schema_name != "weblate-in-context-bindings-v1":
            raise HTTPException(
                status.HTTP_422_UNPROCESSABLE_ENTITY,
                "Unsupported manifest schema",
            )
        manifest_store.replace(manifest)

    @app.get(
        "/v1/review/{project}/{component}/{language}/{context:path}",
        response_model=ReviewUnit,
        dependencies=[Depends(require_review_session)],
    )
    async def get_review_unit(
        project: str, component: str, language: str, context: str
    ) -> ReviewUnit:
        binding = manifest_store.get_binding(project, component, context)
        if binding is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Binding not found")
        target = binding.targets.get(language)
        if target is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Target language not found")
        unit = await client.get_unit(target.unit_id)
        if unit.get("content_hash") != target.content_hash:
            raise HTTPException(status.HTTP_409_CONFLICT, "Binding is stale")
        return ReviewUnit(binding=binding, unit=unit)

    @app.post(
        "/v1/comments/{project}/{component}/{language}/{context:path}",
        dependencies=[Depends(require_review_session)],
    )
    async def create_context_comment(
        project: str,
        component: str,
        language: str,
        context: str,
        request: CommentRequest,
    ) -> dict[str, object]:
        binding = manifest_store.get_binding(project, component, context)
        if binding is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Binding not found")
        target = binding.targets.get(language)
        if target is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Target language not found")
        return await client.create_unit_comment(target.unit_id, request.comment)

    @app.post(
        "/v1/screenshots/{project}/{component}/{language}/{context:path}",
        dependencies=[Depends(require_review_session)],
    )
    async def create_context_screenshot(
        project: str,
        component: str,
        language: str,
        context: str,
        image: UploadFile = File(),
    ) -> dict[str, object]:
        binding = manifest_store.get_binding(project, component, context)
        if binding is None or language not in binding.targets:
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Binding not found")
        if image.content_type != "image/png":
            raise HTTPException(
                status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, "Screenshot must be PNG"
            )
        content = await image.read(8 * 1024 * 1024 + 1)
        if len(content) > 8 * 1024 * 1024:
            raise HTTPException(
                status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                "Screenshot exceeds 8 MB",
            )
        source_unit = await client.get_unit(binding.source_unit_id)
        source_language = source_unit.get("language_code")
        if not isinstance(source_language, str):
            raise HTTPException(
                status.HTTP_502_BAD_GATEWAY, "Invalid source unit response"
            )
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        screenshot = await client.create_screenshot(
            project=project,
            component=component,
            language=source_language,
            name=f"{context} - {timestamp}"[:200],
            image=content,
        )
        screenshot_id = screenshot.get("id")
        if not isinstance(screenshot_id, int):
            screenshot_url = screenshot.get("url")
            match = (
                re.search(r"/api/screenshots/(?P<id>[0-9]+)/?$", screenshot_url)
                if isinstance(screenshot_url, str)
                else None
            )
            if match:
                screenshot_id = int(match.group("id"))
        if not isinstance(screenshot_id, int):
            raise HTTPException(
                status.HTTP_502_BAD_GATEWAY, "Invalid screenshot response"
            )
        result = await client.associate_screenshot_unit(
            screenshot_id, binding.source_unit_id
        )
        return {
            "id": screenshot_id,
            "name": screenshot.get("name"),
            "file_url": screenshot.get("file_url"),
            "url": screenshot.get("url"),
            "units": result.get("units", []),
        }

    return app


def create_app_from_environment() -> FastAPI:
    return create_app(Settings.from_environment())
