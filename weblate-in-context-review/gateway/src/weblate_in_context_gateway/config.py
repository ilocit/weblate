# Copyright © 2026 Weblate authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Settings:
    weblate_url: str
    weblate_api_token: str | None
    manifest_secret: str
    review_session_token: str
    allowed_origins: tuple[str, ...] = ()

    @classmethod
    def from_environment(cls) -> Settings:
        return cls(
            weblate_url=os.environ["WEBLATE_URL"].rstrip("/"),
            weblate_api_token=os.environ.get("WEBLATE_API_TOKEN") or None,
            manifest_secret=os.environ["MANIFEST_SECRET"],
            review_session_token=os.environ["REVIEW_SESSION_TOKEN"],
            allowed_origins=tuple(
                origin.strip()
                for origin in os.environ.get("REVIEW_ALLOWED_ORIGINS", "").split(",")
                if origin.strip()
            ),
        )
