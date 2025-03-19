"""Main entry point to the app"""

import os
import re
import logging
import logging.config
import importlib.metadata
from dotenv import load_dotenv
from app.parser import CommandInput

load_dotenv()
dummy_key = os.getenv("DUMMY_API_KEY")

os.makedirs('logs', exist_ok=True)
logging.config.fileConfig("logging.conf", disable_existing_loggers=False)

plugins = {}
for entry_point in importlib.metadata.entry_points(group="calculator.plugins"):
    plugin_cls = entry_point.load()
    plugins[entry_point.name] = plugin_cls

exit_str = re.compile(r"^\s*(exit|quit|q)", re.IGNORECASE)

logging.info(f"Plugins loaded: {plugins}")


while True:
    try:
        cmd = CommandInput(input(">>> "))

        if exit_str.match(cmd.command):
            logging.debug("Recieved exit command")
            break

        plg = []
        for plugin in plugins.values():
            if plugin.in_scope(cmd):
                logging.debug(f"Plugin {plugin} in scope")
                plg.append(plugin)

        if len(plg) == 0:
            logging.error("Unrecognized command: {cmd.command}")
            print(f">>> Unrecognized command: {cmd.command}")
        elif len(plg) > 1:
            logging.error(f"Multiple plugins in scope for {cmd}: {plg}")
            print(f">>> Amibiguous command: {cmd.command}")
        else:
            logging.debug(f"Executing {cmd.command} using {plg[0]}")
            print(f">>> {plg[0](cmd).execute()}")

    except (EOFError, KeyboardInterrupt):
        break
