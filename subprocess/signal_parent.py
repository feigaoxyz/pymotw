import os
import signal
import subprocess
import time
import sys

proc = subprocess.Popen(
    ['python3', 'signal_child.py'],
    shell=True,
)
print('PROC ID {:>6}'.format(proc.pid))
sys.stdout.flush()

print('PARENT: Pausing before sending signal...')
sys.stdout.flush()
time.sleep(1)

print('PARENT: Signaling child')
sys.stdout.flush()

os.kill(proc.pid, signal.SIGUSR1)
