import subprocess
import pickle

def unsafe_pickle(data):
    # VULNERABLE: Arbitrary code execution
    return pickle.loads(data)

def run_command(cmd):
    # VULNERABLE: Command injection
    return subprocess.check_output(cmd, shell=True)  # UNSAFE: Shell=True