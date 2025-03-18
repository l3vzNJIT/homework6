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
        plg = []
        for plugin in plugins.values():
            if plugin.in_scope(cmd):
                print(f">>> Plugin {plugin} in scope")
                plg.append(plugin)
        if len(plg) == 0:
            print(f">>> Unrecognized command: {cmd.command}")
        elif len(plg) > 1:
            print(f">>> Amibiguous command: {cmd.command}")
        else:
            print(f">>> {plg[0](cmd).execute()}")
    except (EOFError, KeyboardInterrupt):
        break
