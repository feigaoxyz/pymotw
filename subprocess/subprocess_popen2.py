import subprocess
"""
To set up the Popen instance for reading and writing at the same time,
use a combination of the previous techniques.

This sets up the pipe to mimic popen2().
"""

print('popen2:')

proc = subprocess.Popen(
    ['cat', '-'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)
msg = 'through stdin to stdout'.encode('utf-8')
stdout_value = proc.communicate(msg)[0].decode('utf-8')

print('pass through:', repr(stdout_value))
