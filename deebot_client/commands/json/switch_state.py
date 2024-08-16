"""Switch state commands."""

from __future__ import annotations

from deebot_client.events import SwitchStateEvent

from .common import GetEnableCommand, SetEnableCommand


class GetSwitchState(GetEnableCommand):
    """Get switch state command."""

    name = "getSwitchState"
    event_type = SwitchStateEvent
    _field_name = "kickClean"


class SetSwitchState(SetEnableCommand):
    """Set switch state command."""

    name = "setSwitchState"
    get_command = GetSwitchState
    _field_name = "kickClean"
