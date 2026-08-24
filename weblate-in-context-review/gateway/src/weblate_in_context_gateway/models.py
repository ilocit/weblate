# Copyright © 2026 Weblate authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class TargetBinding(BaseModel):
    model_config = ConfigDict(extra="forbid")

    unit_id: int
    id_hash: int
    content_hash: int
    last_updated: str
    web_url: str


class ResourceBinding(BaseModel):
    model_config = ConfigDict(extra="forbid")

    canonical_key: str
    context: str
    source_unit_id: int
    source_id_hash: int
    source_content_hash: int
    source_last_updated: str
    source_web_url: str
    targets: dict[str, TargetBinding]


class BindingIssue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    kind: str
    context: str
    unit_ids: tuple[int, ...]


class BindingManifest(BaseModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)

    schema_name: str = Field(alias="schema")
    generated_at: str
    project: str
    component: str
    bindings: tuple[ResourceBinding, ...]
    issues: tuple[BindingIssue, ...]


class ReviewUnit(BaseModel):
    binding: ResourceBinding
    unit: dict[str, object]
