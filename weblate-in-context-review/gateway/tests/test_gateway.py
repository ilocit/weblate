# Copyright © 2026 Weblate authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import json
from unittest import TestCase
from unittest.mock import AsyncMock

from fastapi.testclient import TestClient

from weblate_in_context_gateway.config import Settings
from weblate_in_context_gateway.main import create_app, sign_payload
from weblate_in_context_gateway.weblate import WeblateClient


def manifest_payload() -> bytes:
    return json.dumps(
        {
            "schema": "weblate-in-context-bindings-v1",
            "generated_at": "2026-08-24T10:00:00+00:00",
            "project": "sample-i18n",
            "component": "messages",
            "bindings": [
                {
                    "canonical_key": "sample-i18n/messages/navigation.home",
                    "context": "navigation.home",
                    "source_unit_id": 101,
                    "source_id_hash": 1101,
                    "source_content_hash": 2101,
                    "source_last_updated": "2026-08-24T10:00:00Z",
                    "source_web_url": "https://weblate.example/source",
                    "targets": {
                        "de": {
                            "unit_id": 202,
                            "id_hash": 1202,
                            "content_hash": 2202,
                            "last_updated": "2026-08-24T10:00:00Z",
                            "web_url": "https://weblate.example/target",
                        }
                    },
                }
            ],
            "issues": [],
        },
        separators=(",", ":"),
        sort_keys=True,
    ).encode()


class GatewayTest(TestCase):
    def setUp(self) -> None:
        self.settings = Settings(
            weblate_url="https://weblate.example",
            weblate_api_token="server-only-token",
            manifest_secret="m" * 32,
            review_session_token="review-token",
        )
        self.weblate_client = AsyncMock()
        self.weblate_client.get_unit.return_value = {
            "id": 202,
            "language_code": "de",
            "content_hash": 2202,
            "source": ["Home"],
            "target": ["Startseite"],
            "state": 20,
        }
        self.client = TestClient(
            create_app(self.settings, weblate_client=self.weblate_client)
        )

    def ingest(self, payload: bytes | None = None) -> None:
        content = payload or manifest_payload()
        response = self.client.post(
            "/v1/manifests",
            content=content,
            headers={
                "Content-Type": "application/json",
                "X-Weblate-Review-Signature": sign_payload(
                    self.settings.manifest_secret, content
                ),
            },
        )
        self.assertEqual(response.status_code, 204)

    def test_rejects_invalid_manifest_signature(self) -> None:
        response = self.client.post(
            "/v1/manifests",
            content=manifest_payload(),
            headers={"X-Weblate-Review-Signature": "sha256=invalid"},
        )

        self.assertEqual(response.status_code, 401)

    def test_resolves_review_unit_without_exposing_weblate_token(self) -> None:
        self.ingest()

        response = self.client.get(
            "/v1/review/sample-i18n/messages/de/navigation.home",
            headers={"Authorization": "Bearer review-token"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["unit"]["target"], ["Startseite"])
        self.assertNotIn("server-only-token", response.text)
        self.weblate_client.get_unit.assert_awaited_once_with(202)

    def test_rejects_stale_binding(self) -> None:
        self.ingest()
        self.weblate_client.get_unit.return_value["content_hash"] = 9999

        response = self.client.get(
            "/v1/review/sample-i18n/messages/de/navigation.home",
            headers={"Authorization": "Bearer review-token"},
        )

        self.assertEqual(response.status_code, 409)

    def test_adds_translation_comment_to_target_unit(self) -> None:
        self.ingest()
        self.weblate_client.create_unit_comment.return_value = {
            "id": 77,
            "comment": "Button label is unclear.",
        }

        response = self.client.post(
            "/v1/comments/sample-i18n/messages/de/navigation.home",
            headers={"Authorization": "Bearer review-token"},
            json={"comment": "Button label is unclear."},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], 77)
        self.weblate_client.create_unit_comment.assert_awaited_once_with(
            202, "Button label is unclear."
        )

        empty_response = self.client.post(
            "/v1/comments/sample-i18n/messages/de/navigation.home",
            headers={"Authorization": "Bearer review-token"},
            json={"comment": "   "},
        )
        self.assertEqual(empty_response.status_code, 422)

    def test_uploads_context_screenshot_and_associates_source_unit(self) -> None:
        self.ingest()
        self.weblate_client.get_unit.return_value = {
            "id": 101,
            "language_code": "en",
        }
        self.weblate_client.create_screenshot.return_value = {
            "name": "navigation.home",
            "file_url": "https://weblate.example/api/screenshots/55/file/",
            "url": "https://weblate.example/api/screenshots/55/",
        }
        self.weblate_client.associate_screenshot_unit.return_value = {
            "units": ["https://weblate.example/api/units/101/"]
        }

        response = self.client.post(
            "/v1/screenshots/sample-i18n/messages/de/navigation.home",
            headers={"Authorization": "Bearer review-token"},
            files={"image": ("context.png", b"png-data", "image/png")},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], 55)
        self.weblate_client.create_screenshot.assert_awaited_once()
        create_arguments = self.weblate_client.create_screenshot.await_args.kwargs
        self.assertEqual(create_arguments["language"], "en")
        self.assertEqual(create_arguments["image"], b"png-data")
        self.weblate_client.associate_screenshot_unit.assert_awaited_once_with(55, 101)

    def test_public_weblate_client_omits_authorization(self) -> None:
        client = WeblateClient("https://weblate.example", None)

        self.assertEqual(client._headers, {})