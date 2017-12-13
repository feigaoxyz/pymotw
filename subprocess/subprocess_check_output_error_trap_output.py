import subprocess
"""
To capture error messages when using `check_output()`, set `stderr` to `STDOUT`,
and the messages will be merged with the rest of the output.
"""

try:
    output = subprocess.check_output(
        'echo to stdout; echo to stderr 1>&2',
        shell=True,
        stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as err:
    print("ERROR:", err)
else:
    print('Have {} bytes in output: {!r}'.format(
        len(output),
        output.decode('utf-8')
    ))
