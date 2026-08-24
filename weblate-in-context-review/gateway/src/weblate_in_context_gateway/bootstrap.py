# Copyright © 2026 Weblate authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import argparse
import hashlib
import hmac
import json
from datetime import datetime, timezone
from typing import Any
from urllib.request import Request, urlopen


def fetch_units(
    weblate_url: str, project: str, component: str, language: str
) -> list[dict[str, Any]]:
    url = (
        f"{weblate_url.rstrip('/')}/api/translations/"
        f"{project}/{component}/{language}/units/"
    )
    units: list[dict[str, Any]] = []
    while url:
        with urlopen(url, timeout=15) as response:  # noqa: S310
            page = json.load(response)
        units.extend(page["results"])
        url = page["next"]
    return units


def build_manifest(
    weblate_url: str,
    project: str,
    component: str,
    source_language: str,
    target_language: str,
) -> dict[str, Any]:
    source_units = {
        unit["context"]: unit
        for unit in fetch_units(weblate_url, project, component, source_language)
        if unit["context"]
    }
    target_units = {
        unit["context"]: unit
        for unit in fetch_units(weblate_url, project, component, target_language)
        if unit["context"]
    }
    bindings = []
    for context, source in sorted(source_units.items()):
        target = target_units.get(context)
        if target is None:
            continue
        bindings.append(
            {
                "canonical_key": f"{project}/{component}/{context}",
                "context": context,
                "source_unit_id": source["id"],
                "source_id_hash": source["id_hash"],
                "source_content_hash": source["content_hash"],
                "source_last_updated": source["last_updated"],
                "source_web_url": source["web_url"],
                "targets": {
                    target_language: {
                        "unit_id": target["id"],
                        "id_hash": target["id_hash"],
                        "content_hash": target["content_hash"],
                        "last_updated": target["last_updated"],
                        "web_url": target["web_url"],
                    }
                },
            }
        )
    return {
        "schema": "weblate-in-context-bindings-v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "project": project,
        "component": component,
        "bindings": bindings,
        "issues": [],
    }


def submit_manifest(gateway_url: str, secret: str, manifest: dict[str, Any]) -> None:
    payload = json.dumps(
        manifest, ensure_ascii=False, separators=(",", ":"), sort_keys=True
    ).encode()
    digest = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    request = Request(
        f"{gateway_url.rstrip('/')}/v1/manifests",
        data=payload,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "X-Weblate-Review-Signature": f"sha256={digest}",
        },
    )
    with urlopen(request, timeout=15) as response:  # noqa: S310
        if response.status != 204:
            msg = f"Gateway returned HTTP {response.status}"
            raise RuntimeError(msg)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--weblate-url", default="http://localhost:8080")
    parser.add_argument("--gateway-url", default="http://localhost:8090")
    parser.add_argument("--project", default="sample-i18n")
    parser.add_argument("--component", default="messages")
    parser.add_argument("--source-language", default="en")
    parser.add_argument("--target-language", default="de")
    parser.add_argument("--secret", required=True)
    arguments = parser.parse_args()
    manifest = build_manifest(
        arguments.weblate_url,
        arguments.project,
        arguments.component,
        arguments.source_language,
        arguments.target_language,
    )
    submit_manifest(arguments.gateway_url, arguments.secret, manifest)
    print(f"Published {len(manifest['bindings'])} bindings.")


if __name__ == "__main__":
    main()