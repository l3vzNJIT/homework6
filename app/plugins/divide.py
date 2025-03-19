"""Plugin for the division command - divides the arguments together and returns the result.

Uses decimal data type.
"""

import re
import logging
from decimal import Decimal
from app.plugin_base import Plugin
from app.parser import CommandInput, CommandOutput


class Divide(Plugin):
    """Add the arguments together"""
    # command string regex this plugin will be responsible for
    # ignore leading whitespace, make it case insensitive
    COMMAND_PATTERN = re.compile(r"^\s*(divide|over|\%|\/|division|div|d)$", re.IGNORECASE)

    def __init__(self, cmd: CommandInput) -> None:
        self.cmd = cmd
        logging.debug("Divide plugin object initialized")

    @classmethod
    def in_scope(cls, cmd: CommandInput) -> bool:
        """Return T/F if the command is in this plugin's scope"""
        logging.debug(f"Divide plugin scope check for {cmd.command}")
        return bool(cls.COMMAND_PATTERN.match(cmd.command))

    def execute(self) -> CommandOutput:
        """Subtract arguments together, return CommandOutput with sum"""
        logging.debug(f"Divideing {self.cmd.args.values()}")

        out_div = None

        for i in range(1, self.cmd.num_args + 1):
            if i == 1:
                out_div = Decimal(self.cmd.args[f"argument_{i}"])
            else:
                out_div /= Decimal(self.cmd.args[f"argument_{i}"])

        logging.debug(f"Returning quotient {out_div}")
        return CommandOutput(str(out_div))
