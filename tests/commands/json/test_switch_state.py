"""Tests regarding switch state commands."""

from __future__ import annotations

import pytest

from deebot_client.commands.json import GetSwitchState, SetSwitchState
from deebot_client.events import SwitchStateEvent
from tests.helpers import get_request_json, get_success_body

from . import assert_command, assert_set_enable_command


@pytest.mark.parametrize("value", [False, True])
async def test_GetSwitchState(*, value: bool) -> None:
    """Testing get switch state."""
    json = get_request_json(get_success_body({"kickClean": 1 if value else 0}))
    await assert_command(GetSwitchState(), json, SwitchStateEvent(value))


@pytest.mark.parametrize("value", [False, True])
async def test_SetSwitchState(*, value: bool) -> None:
    """Testing set switch state."""
    await assert_set_enable_command(
        SetSwitchState(value), SwitchStateEvent, enabled=value, field_name="kickClean"
    )
