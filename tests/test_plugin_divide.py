"""Tests for the division plugin"""

from decimal import Decimal
import pytest
from app.parser import CommandInput, CommandOutput
from app.plugins.divide import Divide


def test_basic_division():
    """Test 1/1 = 1"""
    command = "divide 1 1"
    assert Divide.in_scope(CommandInput(command))
    output = Divide(CommandInput("divide 1 1")).execute()
    assert str(output) == "1"


@pytest.mark.parametrize("cmd", ["divide", "dIv", "/", "over", "dIvISION"])

def test_valid_command_strings(cmd):
    """Verify expected strings are accepted by regex"""
    assert Divide.in_scope(CommandInput(cmd))


def test_division_range(div_input):
    """Test addition on randomized number of randomized arguments"""
    # add_input is a CommandInput type
    assert Divide.in_scope(div_input)
    output = Divide(div_input).execute()
    assert isinstance(output, CommandOutput)
    correct_div = None

    for i in range(1, div_input.num_args + 1):
        if i == 1:
            correct_div = Decimal(div_input.args[f"argument_{i}"])
        else:
            correct_div /= Decimal(div_input.args[f"argument_{i}"])

    assert str(correct_div) == str(output)
