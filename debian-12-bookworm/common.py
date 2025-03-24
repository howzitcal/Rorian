import os
import sys
import datetime

def run_command(command):
    log(f"RUNNING COMMAND: '{command}'")
    if (os.system(command) != 0):
        log(f"COMMAND '{command}' failed.", True)
        raise SystemError(f"Command '{command}' failed.")

def log(message, error=False):
    print(f"[{'LOG' if not error else 'ERROR'}][{datetime.datetime.now()}][{message}]")
