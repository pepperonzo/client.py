"""Cleaning speed event module."""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum, unique

from .base import Event


@unique
class CleaningSpeed(IntEnum):
    """Enum class for all possible cleaning speeds."""

    STANDARD = 0
    DEEP_CLEANING = 1
    QUICK_CLEANING = 2


@dataclass(frozen=True)
class CleaningSpeedEvent(Event):
    """Cleaning speed event representation."""

    sweepMode: CleaningSpeed
