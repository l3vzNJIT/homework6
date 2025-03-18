"""Main entry point to the app"""

import importlib.metadata
from app.parser import CommandInput

plugins = {}
for entry_point in importlib.metadata.entry_points(group="calculator.plugins"):
    plugin_cls = entry_point.load()
    plugins[entry_point.name] = plugin_cls

print(f"Plugins loaded: {plugins}")

while True:
    try:
        cmd = CommandInput(input(">>> "))
        for plugin in plugins.values():
            if plugin.in_scope(cmd):
                print(f"Plugin {plugin} can take care of this for you")
    except (EOFError, KeyboardInterrupt):
        break
