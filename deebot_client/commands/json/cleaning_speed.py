"""Cleaning speed commands."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING, Any

from deebot_client.command import InitParam
from deebot_client.events import CleaningSpeed, CleaningSpeedEvent
from deebot_client.message import HandlingResult
from deebot_client.util import get_enum

from .common import JsonGetCommand, JsonSetCommand

if TYPE_CHECKING:
    from deebot_client.event_bus import EventBus


class GetCleaningSpeed(JsonGetCommand):
    """Get cleaning speed command."""

    name = "onCustomAreaMode"

    @classmethod
    def _handle_body_data_dict(
        cls, event_bus: EventBus, data: dict[str, Any]
    ) -> HandlingResult:
        """Handle message->body->data and notify the correct event subscribers.

        :return: A message response
        """
        event_bus.notify(CleaningSpeedEvent(CleaningSpeed(int(data["sweepMode"]))))
        return HandlingResult.success()


class SetCleaningSpeed(JsonSetCommand):
    """Set cleaning speed command."""

    name = "setCustomAreaMode"
    get_command = GetCleaningSpeed
    _mqtt_params = MappingProxyType({"sweepMode": InitParam(CleaningSpeed)})

    def __init__(self, sweepMode: CleaningSpeed | str) -> None:
        if isinstance(sweepMode, str):
            sweepMode = get_enum(CleaningSpeed, sweepMode)
        super().__init__({"sweepMode": sweepMode.value})
