from __future__ import annotations

from typing import Any

import pytest

from deebot_client.commands.json import GetTrueDetectSensitivity, SetTrueDetectSensitivity
from deebot_client.events import TrueDetectSensitivity, TrueDetectSensitivityEvent
from tests.helpers import (
    get_request_json,
    get_success_body,
)

from . import assert_command, assert_set_command


@pytest.mark.parametrize(
    ("json", "expected"),
    [
        ({"level": 0}, TrueDetectSensitivityEvent(TrueDetectSensitivity.HIGH)),
        ({"level": 1}, TrueDetectSensitivityEvent(TrueDetectSensitivity.STANDARD)),
    ],
)
async def test_GetTrueDetectSensitivity(json: dict[str, Any], expected: TrueDetectSensitivityEvent) -> None:
    json = get_request_json(get_success_body(json))
    await assert_command(GetTrueDetectSensitivity(), json, expected)


@pytest.mark.parametrize(("value"), [TrueDetectSensitivity.HIGH, "high"])
async def test_SetTrueDetectSensitivity(value: TrueDetectSensitivity | str) -> None:
    command = SetTrueDetectSensitivity(value)
    args = {"level": 0}
    await assert_set_command(command, args, TrueDetectSensitivityEvent(TrueDetectSensitivity.HIGH))


def test_SetTrueDetectSensitivity_inexisting_value() -> None:
    with pytest.raises(ValueError, match="'INEXSTING' is not a valid TrueDetectSensitivity member"):
        SetTrueDetectSensitivity("inexsting")
