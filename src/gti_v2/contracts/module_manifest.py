"""Module manifest contract for GTI V2.

Defines the immutable metadata describing a module registered
with the GTI V2 Central Orchestrator.

Architecture Reference:
    ORC-001
"""

from __future__ import annotations

from dataclasses import dataclass


__all__ = (
    "ModuleManifest",
)


@dataclass(frozen=True, slots=True)
class ModuleManifest:
    """Immutable module registration contract."""

    module_id: str
    module_name: str
    module_version: str

    enabled: bool

    retry_limit: int

    supports_rollback: bool

    supports_replay: bool
