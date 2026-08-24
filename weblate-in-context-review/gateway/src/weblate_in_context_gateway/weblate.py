# Copyright © 2026 Weblate authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import httpx


class WeblateClient:
    def __init__(self, base_url: str, api_token: str | None) -> None:
        self._base_url = base_url.rstrip("/")
        self._headers = (
            {"Authorization": f"Token {api_token}"} if api_token else {}
        )

    async def get_unit(self, unit_id: int) -> dict[str, object]:
        async with httpx.AsyncClient(
            base_url=self._base_url, headers=self._headers, timeout=15
        ) as client:
            response = await client.get(f"/api/units/{unit_id}/")
            response.raise_for_status()
            return response.json()

    async def create_unit_comment(
        self, unit_id: int, comment: str
    ) -> dict[str, object]:
        async with httpx.AsyncClient(
            base_url=self._base_url, headers=self._headers, timeout=15
        ) as client:
            response = await client.post(
                f"/api/units/{unit_id}/comments/",
                json={"scope": "translation", "comment": comment},
            )
            response.raise_for_status()
            return response.json()

    async def create_screenshot(
        self,
        *,
        project: str,
        component: str,
        language: str,
        name: str,
        image: bytes,
    ) -> dict[str, object]:
        async with httpx.AsyncClient(
            base_url=self._base_url, headers=self._headers, timeout=30
        ) as client:
            response = await client.post(
                "/api/screenshots/",
                data={
                    "project_slug": project,
                    "component_slug": component,
                    "language_code": language,
                    "name": name,
                },
                files={"image": ("context.png", image, "image/png")},
            )
            response.raise_for_status()
            return response.json()

    async def associate_screenshot_unit(
        self, screenshot_id: int, unit_id: int
    ) -> dict[str, object]:
        async with httpx.AsyncClient(
            base_url=self._base_url, headers=self._headers, timeout=15
        ) as client:
            response = await client.post(
                f"/api/screenshots/{screenshot_id}/units/",
                json={"unit_id": unit_id},
            )
            response.raise_for_status()
            return response.json()
