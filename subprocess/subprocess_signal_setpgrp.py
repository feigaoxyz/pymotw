import os
import signal
import tempfile
import subprocess
import time
import sys

"""
To send signals to descendants without knowing their process id,
use a process group to associate the children so they can be signaled together.

os.setpgrp() should not be called in the same process where the Popen is
created. Instead, the function is passed to Popen as the preexec_fn argument
so it is run after the fork() inside the new process, before it uses exec()
to run the shell. To signal the entire process group, use os.killpg() with
the pid value from the Popen instance.

The sequence of events is:
    The parent program instantiates Popen.
    The Popen instance forks a new process.
    The new process runs os.setpgrp().
    The new process runs exec() to start the shell.
    The shell runs the shell script.
    The shell script forks again and that process execs Python.
    Python runs signal_child.py.
    The parent program signals the process group using the pid of the shell.
    The shell and Python processes receive the signal.
    The shell ignores the signal.
    The Python process running signal_child.py invokes the signal handler.
"""


def show_setting_prgrp():
    print('Calling os.setpgrp() from {}'.format(os.getpid()))
    os.setpgrp()
    print('Process group is now {}'.format(
        os.getpid(), os.getpgrp()
    ))
    sys.stdout.flush()


script = """#!/bin/sh
echo "shell script in process $$"
set -x
python3 signal_child.py
"""

script_file = tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()

proc = subprocess.Popen(
    ['sh', script_file.name],
    preexec_fn=show_setting_prgrp,
)

print('Parent   : Pausing before signaling {}...'.format(proc.pid))
sys.stdout.flush()
time.sleep(1)

print('Parent   : Signaling process group {}'.format(
    proc.pid
))
sys.stdout.flush()

os.killpg(proc.pid, signal.SIGUSR1)
time.sleep(3)
