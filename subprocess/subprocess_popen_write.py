import subprocess
"""
To set up a pipe to allow the calling program to write data to it,
set `stdin` to `PIPE`.

To send data to the standard input channel of the process one time,
pass the data to `communicate()`.
This is similar to using `popen()` with mode `w`.
"""

print('write:')

proc = subprocess.Popen(['cat', '-'], stdin=subprocess.PIPE)
proc.communicate('stdin: to stdin\n'.encode('utf-8'))
