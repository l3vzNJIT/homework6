"""Module defining abstract plugin class and any plugin-wide objects.

Plugins are used to implement commands in the command pattern design of the REPL.
"""

from abc import ABC, abstractmethod
from app.parser import CommandInput, CommandOutput


class Plugin(ABC):
    """Plugin astract base class"""
    @classmethod
    @abstractmethod
    def in_scope(cls, cmd: CommandInput) -> bool:
        """Validates if this plugin handles the given input"""
        raise NotImplementedError("in_scope must be implemented by subclass")

    @abstractmethod
    def execute(self) -> CommandOutput:
        """Executes the functionality of this command"""
        raise NotImplementedError("execute must be implemented by subclass")
