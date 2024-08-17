from __future__ import annotations

from typing import Any

import pytest

from deebot_client.commands.json import GetCleaningSpeed, SetCleaningSpeed
from deebot_client.events import CleaningSpeed, CleaningSpeedEvent
from tests.helpers import (
    get_request_json,
    get_success_body,
)

from . import assert_command, assert_set_command


@pytest.mark.parametrize(
    ("json", "expected"),
    [
        ({"sweepMode": 0}, CleaningSpeedEvent(CleaningSpeed.STANDARD)),
        ({"sweepMode": 1}, CleaningSpeedEvent(CleaningSpeed.DEEP_CLEANING)),
        ({"sweepMode": 2}, CleaningSpeedEvent(CleaningSpeed.QUICK_CLEANING)),
    ],
)
async def test_GetCleaningSpeed(json: dict[str, Any], expected: CleaningSpeedEvent) -> None:
    json = get_request_json(get_success_body(json))
    await assert_command(GetCleaningSpeed(), json, expected)


@pytest.mark.parametrize(("value"), [CleaningSpeed.DEEP_CLEANING, "deep_cleaning"])
async def test_SetCleaningSpeed(value: CleaningSpeed | str) -> None:
    command = SetCleaningSpeed(value)
    args = {"sweepMode": 1}
    await assert_set_command(command, args, CleaningSpeedEvent(CleaningSpeed.DEEP_CLEANING))


def test_SetCleaningSpeed_inexisting_value() -> None:
    with pytest.raises(ValueError, match="'INEXSTING' is not a valid CleaningSpeed member"):
        SetCleaningSpeed("inexsting")
