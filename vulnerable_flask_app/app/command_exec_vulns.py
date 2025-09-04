import subprocess
import os

def subprocess_run_shell(command):
    # VULNERABLE: Command injection with shell=True
    return subprocess.run(command, shell=True)

def os_system(command):
    # VULNERABLE: Command injection
    return os.system(command)

def os_popen(command):
    # VULNERABLE: Command injection
    return os.popen(command)