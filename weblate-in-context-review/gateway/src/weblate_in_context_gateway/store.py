# Copyright © 2026 Weblate authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from weblate_in_context_gateway.models import BindingManifest, ResourceBinding


class ManifestStore:
    def __init__(self) -> None:
        self._manifests: dict[tuple[str, str], BindingManifest] = {}
        self._bindings: dict[tuple[str, str, str], ResourceBinding] = {}

    def replace(self, manifest: BindingManifest) -> None:
        component_key = (manifest.project, manifest.component)
        stale_keys = [key for key in self._bindings if key[:2] == component_key]
        for key in stale_keys:
            del self._bindings[key]

        self._manifests[component_key] = manifest
        for binding in manifest.bindings:
            self._bindings[
                (manifest.project, manifest.component, binding.context)
            ] = binding

    def get_binding(
        self, project: str, component: str, context: str
    ) -> ResourceBinding | None:
        return self._bindings.get((project, component, context))
