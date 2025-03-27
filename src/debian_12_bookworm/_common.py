import os
import sys
import datetime

args = sys.argv


def run_command(command, op=False, can_fail=False):
    log(f"RUNNING COMMAND: '{command}'")
    if not op:
        if os.system(command) != 0 and can_fail == False:
            log(f"COMMAND '{command}' FAILED.", True)
            raise SystemError(f"Command '{command}' failed.")
        log(f"COMMAND '{command}' RAN SUCCESSFULLY.")
    else:
        output = os.popen(command)
        log(f"COMMAND '{command}' RAN.")
        return output.read()


def log(message, error=False):
    print(f"[{'LOG' if not error else 'ERROR'}][{datetime.datetime.now()}][{message}]")


def get_arg(check):
    for arg in args:
        if arg.startswith(check):
            return arg
    return False
