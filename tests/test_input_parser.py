""" Tests for the input string parser
"""

import pytest
from app.input_parser import CommandInput
from tests.conftest import gen_rnd_cmd


def test_parser():
    """ Test a command with two arguments """
    command1 = "add 1 1"
    parsed_command = CommandInput(command1)
    assert parsed_command.input_string == command1, "input string"
    assert parsed_command.command == "add", "input command"
    assert parsed_command.num_args == 2, "input num_args"
    assert parsed_command.args["argument_1"] == "1", "arg 1"
    assert parsed_command.args["argument_2"] == "1", "arg 2"


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
    parsed_command = CommandInput(example_command["input_str"])
    assert parsed_command.input_string == example_command["input_str"], "input_str"
    assert parsed_command.command == example_command["command"], "command"
    assert parsed_command.num_args == example_command["num_args"], "num_args"
    assert parsed_command.args["argument_1"] == example_command["args"]["argument_1"], "arg1"
    assert parsed_command.args["argument_2"] == example_command["args"]["argument_2"], "arg2"
    assert parsed_command.args["argument_3"] == example_command["args"]["argument_3"], "arg3"


@pytest.fixture
def ex_rnd_cmd():
    """ Wrap a random command generation into a fixtrue """
    return gen_rnd_cmd()


def test_with_random_fixture(ex_rnd_cmd):  # pylint: disable=redefined-outer-name
    """ Test the CommandInput parser with a randomized fixture """
    parsed_command = CommandInput(ex_rnd_cmd["input_str"])
    assert parsed_command.input_string == ex_rnd_cmd["input_str"], "input_str"
    assert parsed_command.command == ex_rnd_cmd["command"], "command"
    assert parsed_command.num_args == ex_rnd_cmd["num_args"], "num_args"
    for i in range(1, ex_rnd_cmd["num_args"] + 1):
        assert parsed_command.args[f"argument_{i}"] == \
            ex_rnd_cmd["args"][f"argument_{i}"], f"arg{i}"


# set up 10 test cases
batch_of_tests = []
for _ in range(10):
    batch_of_tests.append(gen_rnd_cmd())
@pytest.mark.parametrize("command_input", batch_of_tests)

def test_with_random_commands(command_input):
    """ Test the CommandInput parser with a randomized fixture """
    parsed_command = CommandInput(command_input["input_str"])
    assert parsed_command.input_string == command_input["input_str"], "input_str"
    assert parsed_command.command == command_input["command"], "command"
    assert parsed_command.num_args == command_input["num_args"], "num_args"
    for i in range(1, command_input["num_args"] + 1):
        assert parsed_command.args[f"argument_{i}"] == \
            command_input["args"][f"argument_{i}"], f"arg{i}"


def test_with_random_cli_commands(cli_input):
    """ Test the CommandInput parser with a randomized fixture """
    parsed_command = CommandInput(cli_input["input_str"])
    assert parsed_command.input_string == cli_input["input_str"], "input_str"
    assert parsed_command.command == cli_input["command"], "command"
    assert parsed_command.num_args == cli_input["num_args"], "num_args"
    for i in range(1, cli_input["num_args"] + 1):
        assert parsed_command.args[f"argument_{i}"] == \
            cli_input["args"][f"argument_{i}"], f"arg{i}"
