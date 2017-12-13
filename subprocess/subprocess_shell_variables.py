"""
setting `shell` argument to a true value cause `subprocess` to spawn an
intermediate shell process which then runs the command.

Using `run()` without `check=True` is equivalent to using `call()`.
"""

import subprocess

completed = subprocess.run('echo $HOME', shell=True)
print('returncode:', completed.returncode)
