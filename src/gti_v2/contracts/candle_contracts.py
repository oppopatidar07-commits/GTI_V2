"""Candle data contract for GTI V2.

This module provides the immutable data contract representing a single
market candle within the GTI V2 trading engine.
"""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from .shared_types import CandleStatus, Instrument, Timeframe

__all__ = ("Candle",)


@dataclass(frozen=True, slots=True)
class Candle:
    """Immutable value object representing a single market candle."""

    instrument: Instrument
    timeframe: Timeframe
    candle_open_time: datetime
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int
    status: CandleStatus
