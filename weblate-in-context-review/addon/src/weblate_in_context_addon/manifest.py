# Copyright © 2026 Weblate authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any, Iterable


@dataclass(frozen=True, slots=True)
class UnitRecord:
    unit_id: int
    language: str
    context: str
    source: tuple[str, ...]
    target: tuple[str, ...]
    id_hash: int
    content_hash: int
    last_updated: str
    web_url: str
    is_source: bool = False


@dataclass(frozen=True, slots=True)
class BindingIssue:
    kind: str
    context: str
    unit_ids: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class TargetBinding:
    unit_id: int
    id_hash: int
    content_hash: int
    last_updated: str
    web_url: str


@dataclass(frozen=True, slots=True)
class ResourceBinding:
    canonical_key: str
    context: str
    source_unit_id: int
    source_id_hash: int
    source_content_hash: int
    source_last_updated: str
    source_web_url: str
    targets: dict[str, TargetBinding]


@dataclass(frozen=True, slots=True)
class BindingManifest:
    schema: str
    generated_at: str
    project: str
    component: str
    bindings: tuple[ResourceBinding, ...]
    issues: tuple[BindingIssue, ...]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def make_canonical_key(project: str, component: str, context: str) -> str:
    return "/".join((project, component, context))


def build_manifest(
    project: str,
    component: str,
    units: Iterable[UnitRecord],
    *,
    generated_at: datetime | None = None,
) -> BindingManifest:
    grouped: dict[str, list[UnitRecord]] = {}
    issues: list[BindingIssue] = []
    for unit in units:
        if not unit.context:
            issues.append(BindingIssue("missing-context", "", (unit.unit_id,)))
            continue
        grouped.setdefault(unit.context, []).append(unit)

    bindings: list[ResourceBinding] = []
    for context, candidates in sorted(grouped.items()):
        source_units = [unit for unit in candidates if unit.is_source]
        if len(source_units) != 1:
            issues.append(
                BindingIssue(
                    "ambiguous-source",
                    context,
                    tuple(sorted(unit.unit_id for unit in source_units)),
                )
            )
            continue

        source_unit = source_units[0]
        targets: dict[str, TargetBinding] = {}
        duplicate_ids: list[int] = []
        for unit in candidates:
            if unit.is_source:
                continue
            if unit.language in targets:
                duplicate_ids.extend((targets[unit.language].unit_id, unit.unit_id))
                continue
            targets[unit.language] = TargetBinding(
                unit_id=unit.unit_id,
                id_hash=unit.id_hash,
                content_hash=unit.content_hash,
                last_updated=unit.last_updated,
                web_url=unit.web_url,
            )
        if duplicate_ids:
            issues.append(
                BindingIssue(
                    "duplicate-target-language",
                    context,
                    tuple(sorted(set(duplicate_ids))),
                )
            )
            continue

        bindings.append(
            ResourceBinding(
                canonical_key=make_canonical_key(project, component, context),
                context=context,
                source_unit_id=source_unit.unit_id,
                source_id_hash=source_unit.id_hash,
                source_content_hash=source_unit.content_hash,
                source_last_updated=source_unit.last_updated,
                source_web_url=source_unit.web_url,
                targets=targets,
            )
        )

    timestamp = generated_at or datetime.now(timezone.utc)
    return BindingManifest(
        schema="weblate-in-context-bindings-v1",
        generated_at=timestamp.isoformat(),
        project=project,
        component=component,
        bindings=tuple(bindings),
        issues=tuple(issues),
    )
