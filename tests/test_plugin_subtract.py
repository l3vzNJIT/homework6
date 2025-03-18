"""Tests for the subtract plugin"""

from decimal import Decimal
import pytest
from app.parser import CommandInput, CommandOutput
from app.plugins.subtract import Subtract


def test_basic_subtraction():
    """Test 1-1 = 0"""
    command = "subtract 1 1"
    assert Subtract.in_scope(CommandInput(command))
    output = Subtract(CommandInput("subtract 1 1")).execute()
    assert str(output) == "0"


@pytest.mark.parametrize("cmd", ["subtract", "Sub", "-", "minus", "sUbTrAcTiOn"])

def test_valid_command_strings(cmd):
    """Verify expected strings are accepted by regex"""
    assert Subtract.in_scope(CommandInput(cmd))


def test_subtraction_range(sub_input):
    """Test addition on randomized number of randomized arguments"""
    # add_input is a CommandInput type
    assert Subtract.in_scope(sub_input)
    output = Subtract(sub_input).execute()
    assert isinstance(output, CommandOutput)
    correct_diff = None
    for i in range(1, sub_input.num_args + 1):
        if i == 1:
            correct_diff = Decimal(sub_input.args[f"argument_{i}"])
        else:
            correct_diff -= Decimal(sub_input.args[f"argument_{i}"])
    assert str(correct_diff) == str(output)
