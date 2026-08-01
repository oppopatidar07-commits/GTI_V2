"""Shared domain types and enumerations for GTI V2.

This module serves as the single source of truth for fundamental shared
closed-value types across all layers of the GTI V2 system.
"""

from enum import StrEnum

__all__ = (
    "Instrument",
    "Timeframe",
    "CandleStatus",
    "ValidationStatus",
    "GapStatus",
    "TrendState",
    "StructureLevel",
    "EventPriority",
    "Environment",
)


class Instrument(StrEnum):
    """Supported financial instruments and market indices."""

    NIFTY = "NIFTY"
    BANKNIFTY = "BANKNIFTY"
    SENSEX = "SENSEX"


class Timeframe(StrEnum):
    """Supported chart timeframes for data aggregation and analysis."""

    MINUTE_1 = "MINUTE_1"
    MINUTE_2 = "MINUTE_2"
    MINUTE_3 = "MINUTE_3"
    MINUTE_5 = "MINUTE_5"
    MINUTE_10 = "MINUTE_10"
    MINUTE_15 = "MINUTE_15"
    MINUTE_30 = "MINUTE_30"
    MINUTE_45 = "MINUTE_45"
    MINUTE_60 = "MINUTE_60"
    MINUTE_75 = "MINUTE_75"
    MINUTE_90 = "MINUTE_90"
    MINUTE_120 = "MINUTE_120"
    MINUTE_180 = "MINUTE_180"
    MINUTE_240 = "MINUTE_240"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"


class CandleStatus(StrEnum):
    """Lifecycle status of a market candle."""

    FORMING = "FORMING"
    CLOSED = "CLOSED"


class ValidationStatus(StrEnum):
    """Validation state of data records and domain entities."""

    VALID = "VALID"
    INVALID = "INVALID"
    QUARANTINED = "QUARANTINED"


class GapStatus(StrEnum):
    """Status of data continuity and gap conditions."""

    NO_GAP = "NO_GAP"
    GAP_DETECTED = "GAP_DETECTED"
    GAP_AFFECTED = "GAP_AFFECTED"


class TrendState(StrEnum):
    """Directional state of market trends."""

    BULLISH = "BULLISH"
    BEARISH = "BEARISH"
    UNDETERMINED = "UNDETERMINED"


class StructureLevel(StrEnum):
    """Classification level of market structure elements."""

    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"


class EventPriority(StrEnum):
    """Priority levels for system events and message queue processing."""

    LOW = "LOW"
    NORMAL = "NORMAL"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class Environment(StrEnum):
    """Runtime execution environment."""

    DEVELOPMENT = "DEVELOPMENT"
    TESTING = "TESTING"
    PRODUCTION = "PRODUCTION"
