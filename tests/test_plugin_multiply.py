"""Tests for the multiplication plugin"""

from decimal import Decimal
import pytest
from app.parser import CommandInput, CommandOutput
from app.plugins.multiply import Multiply


def test_basic_multiplication():
    """Test 1*1 = 1"""
    command = "multiply 1 1"
    assert Multiply.in_scope(CommandInput(command))
    output = Multiply(CommandInput("multiply 1 1")).execute()
    assert str(output) == "1"


@pytest.mark.parametrize("cmd", ["multiply", "Mult", "*", "times", "MuLtIplicATION"])

def test_valid_command_strings(cmd):
    """Verify expected strings are accepted by regex"""
    assert Multiply.in_scope(CommandInput(cmd))


def test_multiplication_range(mult_input):
    """Test addition on randomized number of randomized arguments"""
    # add_input is a CommandInput type
    assert Multiply.in_scope(mult_input)
    output = Multiply(mult_input).execute()
    assert isinstance(output, CommandOutput)
    correct_mult = None

    for i in range(1, mult_input.num_args + 1):
        if i == 1:
            correct_mult = Decimal(mult_input.args[f"argument_{i}"])
        else:
            correct_mult *= Decimal(mult_input.args[f"argument_{i}"])

    assert str(correct_mult) == str(output)
