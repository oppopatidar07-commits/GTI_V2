"""Module registry contract for GTI V2.

Defines the immutable registry containing every module
registered with the GTI V2 Central Orchestrator.

Architecture Reference:
    ORC-001
"""

from __future__ import annotations

from dataclasses import dataclass

from .module_manifest import ModuleManifest

__all__ = (
    "ModuleRegistry",
)


@dataclass(frozen=True, slots=True)
class ModuleRegistry:
    """Immutable collection of registered GTI V2 modules."""

    modules: tuple[ModuleManifest, ...]
