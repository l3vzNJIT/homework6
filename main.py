"""Main entry point to the app"""

import os
import re
import importlib.metadata
from dotenv import load_dotenv
from app.parser import CommandInput

load_dotenv()
dummy_key = os.getenv("DUMMY_API_KEY")
print(f"Dummy key: {dummy_key}")

plugins = {}
for entry_point in importlib.metadata.entry_points(group="calculator.plugins"):
    plugin_cls = entry_point.load()
    plugins[entry_point.name] = plugin_cls

print(f"Plugins loaded: {plugins}")

exit_str = re.compile(r"^\s*(exit|quit)", re.IGNORECASE)

while True:
    try:
        cmd = CommandInput(input(">>> "))

        if exit_str.match(cmd.command):
            break

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
