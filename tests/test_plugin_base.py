"""Base class test module."""

import pytest
from app.parser import CommandInput
from app.plugin_base import Plugin


class DummyPlugin(Plugin):
    """Concrete implementation of Plugin just for testing coverage"""
    @classmethod
    def in_scope(cls, cmd):
        return super().in_scope(cmd)

    def execute(self):  # pylint: disable=useless-parent-delegation
        return super().execute()


def test_dummy_plugin_behavior():
    """Test dummy plugin to ensure Plugin ABC is covered"""
    plugin = DummyPlugin()

    with pytest.raises(NotImplementedError):
        plugin.in_scope(CommandInput("test"))

    with pytest.raises(NotImplementedError):
        plugin.execute()  # pylint: disable=useless-parent-delegation
