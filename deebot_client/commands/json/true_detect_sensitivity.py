"""True detect sensitivity commands."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING, Any

from deebot_client.command import InitParam
from deebot_client.events import TrueDetectSensitivity,TrueDetectSensitivityEvent
from deebot_client.message import HandlingResult
from deebot_client.util import get_enum

from .common import JsonGetCommand, JsonSetCommand

if TYPE_CHECKING:
    from deebot_client.event_bus import EventBus


class GetTrueDetectSensitivity(JsonGetCommand):
    """Get true detect sensitivity info command."""

    name = "getTrueDetect"

    @classmethod
    def _handle_body_data_dict(
        cls, event_bus: EventBus, data: dict[str, Any]
    ) -> HandlingResult:
        """Handle message->body->data and notify the correct event subscribers.

        :return: A message response
        """
        enable = data.get("enable")
        event_bus.notify(
            TrueDetectSensitivityEvent(
                enable=enable,
                TrueDetectSensitivityEvent(int(data["level"])),
            )
        )
        return HandlingResult.success()


class SetTrueDetectSensitivity(JsonSetCommand):
    """Set true detect sensitivity command."""

    name = "setTrueDetect"
    get_command = GetTrueDetectSensitivity
    _mqtt_params = MappingProxyType(
        {
            "enable": InitParam(enable),
            "level": InitParam(TrueDetectSensitivity),
        }
    )

    def __init__(
        self, enable: enable | str, level: TrueDetectSensitivity | str
    ) -> None:
        params = {}
        if isinstance(level, str):
            level = get_enum(TrueDetectSensitivity, level)
        params["level"] = level.value
        super().__init__(params)
