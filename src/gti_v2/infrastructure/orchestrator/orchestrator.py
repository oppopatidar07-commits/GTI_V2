"""GTI V2 Central System Orchestrator.

This module contains the central orchestration engine responsible for
owning the complete execution lifecycle of the GTI V2 trading system.

Architecture Reference:
    ORC-001
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from ...contracts.module_registry import ModuleRegistry


class OrchestratorState(StrEnum):
    """Execution lifecycle states owned by the GTI V2 Orchestrator."""

    STARTUP = "startup"
    INITIALIZATION = "initialization"
    WARMUP = "warmup"
    RUNNING = "running"
    PAUSED = "paused"
    RECOVERY = "recovery"
    STOPPING = "stopping"
    SHUTDOWN = "shutdown"
    RESTART = "restart"


@dataclass(slots=True)
class OrchestratorContext:
    """Runtime context owned by the GTI V2 Central Orchestrator."""

    state: OrchestratorState
    registry: ModuleRegistry


class Orchestrator:
    """Central execution owner of the GTI V2 trading engine."""

    def __init__(self, registry: ModuleRegistry) -> None:
        """Create a new orchestrator instance."""

        self._context = OrchestratorContext(
            state=OrchestratorState.STARTUP,
            registry=registry,
        )
