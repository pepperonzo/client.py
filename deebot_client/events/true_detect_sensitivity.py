"""True detect sensitivity event module."""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum, unique

from .base import Event


@unique
class TrueDetectSensitivity(IntEnum):
    """Enum class for all possible True detect sensitivities."""

    HIGH = 0
    STANDARD = 1


@dataclass(frozen=True)
class TrueDetectSensitivityEvent(Event):
    """True detect sensitivity representation."""

    level: TrueDetectSensitivity
