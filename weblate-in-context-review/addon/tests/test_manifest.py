# Copyright © 2026 Weblate authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from datetime import datetime, timezone
from unittest import TestCase

from weblate_in_context_addon.manifest import UnitRecord, build_manifest
from weblate_in_context_addon.signing import sign_payload, verify_payload


def make_unit(
    unit_id: int,
    language: str,
    context: str,
    *,
    is_source: bool = False,
) -> UnitRecord:
    return UnitRecord(
        unit_id=unit_id,
        language=language,
        context=context,
        source=("Home",),
        target=("Home" if is_source else "Startseite",),
        id_hash=1000 + unit_id,
        content_hash=2000 + unit_id,
        last_updated="2026-08-24T10:00:00Z",
        web_url=f"https://weblate.example/translate/?checksum={unit_id}",
        is_source=is_source,
    )


class ManifestTest(TestCase):
    def test_builds_key_based_binding_for_target_language(self) -> None:
        manifest = build_manifest(
            "sample-i18n",
            "messages",
            (
                make_unit(101, "en", "navigation.home", is_source=True),
                make_unit(202, "de", "navigation.home"),
            ),
            generated_at=datetime(2026, 8, 24, tzinfo=timezone.utc),
        )

        binding = manifest.bindings[0]
        self.assertEqual(
            binding.canonical_key, "sample-i18n/messages/navigation.home"
        )
        self.assertEqual(binding.source_unit_id, 101)
        self.assertEqual(binding.targets["de"].unit_id, 202)
        self.assertEqual(manifest.issues, ())

    def test_reports_keyless_and_ambiguous_units(self) -> None:
        manifest = build_manifest(
            "sample-i18n",
            "messages",
            (
                make_unit(1, "en", ""),
                make_unit(2, "en", "button.save", is_source=True),
                make_unit(3, "en", "button.save", is_source=True),
            ),
        )

        self.assertEqual(manifest.bindings, ())
        self.assertEqual(
            [issue.kind for issue in manifest.issues],
            ["missing-context", "ambiguous-source"],
        )

    def test_manifest_signature_rejects_changed_payload(self) -> None:
        signature = sign_payload("a" * 32, b'{"project":"sample-i18n"}')

        self.assertTrue(
            verify_payload("a" * 32, b'{"project":"sample-i18n"}', signature)
        )
        self.assertFalse(
            verify_payload("a" * 32, b'{"project":"other"}', signature)
        )