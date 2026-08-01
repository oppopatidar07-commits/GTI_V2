"""Module dependency contracts for GTI V2.

Defines immutable dependency relationships between registered
modules inside the GTI V2 Central Orchestrator.

Architecture Reference:
    ORC-001
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


__all__ = (
    "DependencyType",
    "ModuleDependency",
)


class DependencyType(StrEnum):
    """Supported dependency classifications."""

    HARD = "hard"
    SOFT = "soft"


@dataclass(frozen=True, slots=True)
class ModuleDependency:
    """Immutable dependency declaration."""

    source_module_id: str
    target_module_id: str
    dependency_type: DependencyType
