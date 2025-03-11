""" Tests for the input string parser
"""

import pytest
from app.input_parser import CommandInput

def test_parser():
    """ Test a command with two arguments """
    command1 = "add 1 1"
    parsed_command1 = CommandInput(command1)
    assert parsed_command1.input_string == command1
    assert parsed_command1.command == "add"
    assert parsed_command1.num_args == 2
    assert parsed_command1.args["argument_1"] == "1"
    assert parsed_command1.args["argument_2"] == "1"

@pytest.fixture
def example_command():
    """ Define a pytest fixture for a single command """
    return {
            "input_str": "command arg1 arg2 arg3",
            "command": "command",
            "num_args" : 3,
            "args" : {
                     "argument_1": "arg1",
                     "argument_2": "arg2",
                     "argument_3": "arg3"
                     }
            }

def test_with_fixture(example_command):  # pylint: disable=redefined-outer-name
    """ Test the CommandInput parser with a fixture """
    parsed_command1 = CommandInput(example_command["input_str"])
    assert parsed_command1.input_string == example_command["input_str"]
    assert parsed_command1.command == example_command["command"]
    assert parsed_command1.num_args == example_command["num_args"]
    assert parsed_command1.args["argument_1"] == example_command["args"]["argument_1"]
    assert parsed_command1.args["argument_2"] == example_command["args"]["argument_2"]
    assert parsed_command1.args["argument_3"] == example_command["args"]["argument_3"]
