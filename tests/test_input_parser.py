""" Tests for the input string parser
"""

import pytest
from faker import Faker
from app.input_parser import CommandInput


def test_parser():
    """ Test a command with two arguments """
    command1 = "add 1 1"
    parsed_command = CommandInput(command1)
    assert parsed_command.input_string == command1
    assert parsed_command.command == "add"
    assert parsed_command.num_args == 2
    assert parsed_command.args["argument_1"] == "1"
    assert parsed_command.args["argument_2"] == "1"


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
    assert parsed_command.input_string == example_command["input_str"]
    assert parsed_command.command == example_command["command"]
    assert parsed_command.num_args == example_command["num_args"]
    assert parsed_command.args["argument_1"] == example_command["args"]["argument_1"]
    assert parsed_command.args["argument_2"] == example_command["args"]["argument_2"]
    assert parsed_command.args["argument_3"] == example_command["args"]["argument_3"]


def gen_rnd_cmd():
    """ Generate a random command string with Faker """
    fake = Faker()
    fake_command = {"command": fake.word(), "num_args": fake.random_digit()}
    args = []
    fake_command["args"] = {}
    for i in range(1, fake_command["num_args"] + 1):
        fake_command["args"][f"argument_{i}"] = fake.word()
        args.append(fake_command["args"][f"argument_{i}"])
    fake_command["input_str"] = " ".join([fake_command["command"]] + args)
    return fake_command


@pytest.fixture
def ex_rnd_cmd():
    """ Wrap a random command generation into a fixtrue """
    return gen_rnd_cmd()


def test_with_random_fixture(ex_rnd_cmd):  # pylint: disable=redefined-outer-name
    """ Test the CommandInput parser with a randomized fixture """
    parsed_command = CommandInput(ex_rnd_cmd["input_str"])
    assert parsed_command.input_string == ex_rnd_cmd["input_str"]
    assert parsed_command.command == ex_rnd_cmd["command"]
    assert parsed_command.num_args == ex_rnd_cmd["num_args"]
    for i in range(1, ex_rnd_cmd["num_args"] + 1):
        assert parsed_command.args[f"argument_{i}"] == ex_rnd_cmd["args"][f"argument_{i}"]


# set up 100 test cases
batch_of_tests = []
for _ in range(100):
    batch_of_tests.append(gen_rnd_cmd())
@pytest.mark.parametrize("command_input", batch_of_tests)

def test_with_random_commands(command_input):
    """ Test the CommandInput parser with a randomized fixture """
    parsed_command = CommandInput(command_input["input_str"])
    assert parsed_command.input_string == command_input["input_str"]
    assert parsed_command.command == command_input["command"]
    assert parsed_command.num_args == command_input["num_args"]
    for i in range(1, command_input["num_args"] + 1):
        assert parsed_command.args[f"argument_{i}"] == command_input["args"][f"argument_{i}"]
