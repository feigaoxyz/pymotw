import os
import signal
import subprocess
import tempfile
import time
import sys
"""
If the process created by Popen spawns sub-processes, those children
will not receive any signals sent to the parent. That means when using
the shell argument to Popen it will be difficult to cause the command
started in the shell to terminate by sending SIGINT or SIGTERM.
"""

script = """#!/bin/sh
echo "Shell script in process $$"
set -x
python3 signal_child.py
"""

script_file = tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()

proc = subprocess.Popen(['sh', script_file.name])
print('PARENT    : Pausing before signaling {}...'.format(proc.pid))
sys.stdout.flush()

time.sleep(1)

print('PARENT    : Signaling child {}'.format(proc.pid))
sys.stdout.flush()

os.kill(proc.pid, signal.SIGUSR1)

time.sleep(3)
