# Copyright © 2026 Weblate authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from typing import ClassVar, TypedDict

from django import forms
from django.utils.translation import gettext_lazy

from weblate.addons.forms import BaseAddonForm


class ReviewManifestConfiguration(TypedDict):
    gateway_url: str
    secret: str


class ReviewManifestForm(BaseAddonForm[ReviewManifestConfiguration, object]):
    public_configuration_fields: ClassVar[frozenset[str]] = frozenset(
        {"gateway_url"}
    )

    gateway_url = forms.URLField(
        label=gettext_lazy("Review gateway manifest URL"),
        help_text=gettext_lazy(
            "HTTPS endpoint that receives signed in-context binding manifests."
        ),
    )
    secret = forms.CharField(
        label=gettext_lazy("Signing secret"),
        min_length=32,
        widget=forms.PasswordInput(render_value=True),
        help_text=gettext_lazy(
            "Shared secret used only to authenticate manifest deliveries."
        ),
    )
