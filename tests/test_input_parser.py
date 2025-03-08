""" Tests for the input string parser
"""

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
