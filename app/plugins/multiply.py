"""Plugin for the multiplication command - multiplies the arguments together and returns the result.

Uses decimal data type.
"""

import re
from decimal import Decimal
from app.plugin_base import Plugin
from app.parser import CommandInput, CommandOutput


class Multiply(Plugin):
    """Add the arguments together"""
    # command string regex this plugin will be responsible for
    # ignore leading whitespace, make it case insensitive
    COMMAND_PATTERN = re.compile(r"^\s*(multiply|times|\*|multiplication|mult|m)$", re.IGNORECASE)

    def __init__(self, cmd: CommandInput) -> None:
        self.cmd = cmd

    @classmethod
    def in_scope(cls, cmd: CommandInput) -> bool:
        """Return T/F if the command is in this plugin's scope"""
        return bool(cls.COMMAND_PATTERN.match(cmd.command))

    def execute(self) -> CommandOutput:
        """Subtract arguments together, return CommandOutput with sum"""
        out_mult = None

        for i in range(1, self.cmd.num_args + 1):
            if i == 1:
                out_mult = Decimal(self.cmd.args[f"argument_{i}"])
            else:
                out_mult *= Decimal(self.cmd.args[f"argument_{i}"])

        return CommandOutput(str(out_mult))
