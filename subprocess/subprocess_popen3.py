import subprocess
"""
It is also possible watch both of the streams for stdout and stderr,
as with popen3().

Reading from stderr works the same as with stdout. Passing PIPE tells
Popen to attach to the channel, and communicate() reads all of the data
from it before returning.
"""

print('popen3:')
proc = subprocess.Popen(
    'cat -; echo "to stderr" 1>&2',
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
msg = 'through stdin to stdout'.encode('utf-8')
stdout_value, stderr_value = proc.communicate(msg)
print('pass through:', repr(stdout_value.decode('utf-8')))
print('stderr      :', repr(stderr_value.decode('utf-8')))
