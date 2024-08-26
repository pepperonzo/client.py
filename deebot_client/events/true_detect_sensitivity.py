"""True detect sensitivity event module."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum, unique

from .base import Event


@unique
class TrueDetectSensitivity(IntEnum):
    """Enum class for all True detect sensitivities."""

    STANDARD = 1
    HIGH = 0


@dataclass(frozen=True)
class TrueDetectSensitivityEvent(Event):
    """True Detect Sensitivity event representation."""

    enable: bool
    level: TrueDetectSensitivity
