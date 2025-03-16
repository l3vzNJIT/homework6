""" Main entry point to the app
"""

from app.parser import CommandInput

while True:
    try:
        print(CommandInput(input(">>> ")).__dict__)
    except (EOFError, KeyboardInterrupt):
        break
