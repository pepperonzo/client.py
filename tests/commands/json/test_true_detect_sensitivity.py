from __future__ import annotations

import re
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
        (
            {"enable": 1, "level": 0},
            WaterInfoEvent(enable=True, TrueDetectSensitivity.HIGH),
        ),
        (
            {"enable": 1, "level": 1},
            WaterInfoEvent(enable=True, TrueDetectSensitivity.STANDARD),
        ),
        (
            {"enable": 0, "level": 0},
            WaterInfoEvent(enable=False, TrueDetectSensitivity.HIGH),
        ),
        (
            {"enable": 0, "level": 1},
            WaterInfoEvent(enable=False, TrueDetectSensitivity.STANDARD),
        ),
    ],
)
async def test_GetTrueDetectSensitivity(json: dict[str, Any], expected: TrueDetectSensitivityEvent) -> None:
    json = get_request_json(get_success_body(json))
    await assert_command(GetTrueDetectSensitivity(), json, expected)


@pytest.mark.parametrize(("level"), [TrueDetectSensitivity.STANDARD, "standard", None])
async def test_SetTrueDetectSensitivity_TrueDetectSensitivity(
    enable_value: bool, level_value: TrueDetectSensitivity | str
) -> None:
    command = SetTrueDetectSensitivity(enable_value, level_value)
    args = {"level": 1}
    await assert_set_command(
        command,
        args,
        TrueDetectSensitivityEvent(TrueDetectSensitivity.STANDARD),
    )


@pytest.mark.parametrize(
    ("command_values", "error", "error_message"),
    [
        (
            {"bla": "inexsting"},
            TypeError,
            re.escape(
                "SetTrueDetectSensitivity.__init__() got an unexpected keyword argument 'bla'"
            ),
        ),
        (
            {"level": "inexsting"},
            ValueError,
            "'INEXSTING' is not a valid TrueDetectSensitivity member",
        ),
    ],
)
def test_SetTrueDetectSensitivity_inexisting_value(
    command_values: dict[str, Any], error: type[Exception], error_message: str
) -> None:
    with pytest.raises(error, match=error_message):
        SetTrueDetectSensitivity(**command_values)
