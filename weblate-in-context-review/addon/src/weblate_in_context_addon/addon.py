# Copyright © 2026 Weblate authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import json
from typing import TYPE_CHECKING, ClassVar
from urllib.parse import urljoin

from django.conf import settings
from django.utils.translation import gettext_lazy

from weblate.addons.base import BaseAddon
from weblate.addons.events import AddonEvent
from weblate.utils.requests import fetch_validated_url
from weblate.utils.site import get_site_url

from weblate_in_context_addon.forms import (
    ReviewManifestConfiguration,
    ReviewManifestForm,
)
from weblate_in_context_addon.manifest import UnitRecord, build_manifest
from weblate_in_context_addon.signing import sign_payload

if TYPE_CHECKING:
    from weblate.trans.models import Component, Unit


def unit_to_record(unit: Unit, *, is_source: bool, site_url: str) -> UnitRecord:
    return UnitRecord(
        unit_id=unit.pk,
        language=unit.translation.language.code,
        context=unit.context,
        source=tuple(unit.get_source_plurals()),
        target=tuple(unit.get_target_plurals()),
        id_hash=unit.id_hash,
        content_hash=unit.content_hash,
        last_updated=unit.last_updated.isoformat(),
        web_url=urljoin(site_url, unit.get_absolute_url()),
        is_source=is_source,
    )


def build_component_manifest(component: Component):
    site_url = get_site_url()
    records = []
    translations = component.translation_set.select_related("language")
    for translation in translations:
        records.extend(
            unit_to_record(unit, is_source=translation.is_source, site_url=site_url)
            for unit in translation.unit_set.select_related(
                "translation__language"
            ).iterator()
        )
    return build_manifest(component.project.slug, component.slug, records)


class InContextReviewManifestAddon(
    BaseAddon[ReviewManifestConfiguration, ReviewManifestConfiguration]
):
    events: ClassVar[set[AddonEvent]] = {
        AddonEvent.EVENT_COMPONENT_UPDATE,
        AddonEvent.EVENT_INSTALL,
        AddonEvent.EVENT_MANUAL,
    }
    settings_form = ReviewManifestForm
    name = "weblate.in_context_review.manifest"
    verbose = gettext_lazy("In-context review manifest")
    description = gettext_lazy(
        "Publishes signed key-to-unit bindings to an external review gateway."
    )
    icon = "link.svg"

    def publish(self, component: Component) -> dict[str, int | str]:
        manifest = build_component_manifest(component)
        payload = json.dumps(
            manifest.to_dict(), ensure_ascii=False, separators=(",", ":"), sort_keys=True
        ).encode()
        configuration = self.configuration
        response = fetch_validated_url(
            method="post",
            url=configuration["gateway_url"],
            content=payload,
            headers={
                "Content-Type": "application/json",
                "X-Weblate-Review-Signature": sign_payload(
                    configuration["secret"], payload
                ),
            },
            timeout=15,
            allow_private_targets=not settings.WEBHOOK_RESTRICT_PRIVATE,
            private_allowlist=settings.WEBHOOK_PRIVATE_ALLOWLIST,
        )
        return {
            "status_code": response.status_code,
            "bindings": len(manifest.bindings),
            "issues": len(manifest.issues),
        }

    def component_update(
        self, component: Component, activity_log_id: int | None = None
    ) -> dict[str, int | str]:
        return self.publish(component)

    def post_install(
        self,
        component: Component,
        add: bool,
        activity_log_id: int | None = None,
    ) -> dict[str, int | str]:
        return self.publish(component)

    def manual(
        self, component: Component, activity_log_id: int | None = None
    ) -> dict[str, int | str]:
        return self.publish(component)
