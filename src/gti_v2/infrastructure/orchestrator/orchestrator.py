"""GTI V2 Central System Orchestrator.

This module contains the central orchestration engine responsible for
owning the complete execution lifecycle of the GTI V2 trading system.

Architecture Reference:
    ORC-001
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

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
