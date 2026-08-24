# Copyright © 2026 Weblate authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import hashlib
import hmac


def sign_payload(secret: str, payload: bytes) -> str:
    digest = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return f"sha256={digest}"


def verify_payload(secret: str, payload: bytes, signature: str) -> bool:
    return hmac.compare_digest(sign_payload(secret, payload), signature)
