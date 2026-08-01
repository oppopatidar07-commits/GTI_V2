"""Module status contracts for GTI V2.

Defines immutable module runtime status values used by the
GTI V2 Central Orchestrator.

Architecture Reference:
    ORC-001
"""

from __future__ import annotations

from enum import StrEnum


__all__ = (
    "ModuleStatus",
)


class ModuleStatus(StrEnum):
    """Runtime states of a registered module."""

    CREATED = "created"
    INITIALIZING = "initializing"
    READY = "ready"
    RUNNING = "running"
    PAUSED = "paused"
    BLOCKED = "blocked"
    RECOVERY = "recovery"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"
