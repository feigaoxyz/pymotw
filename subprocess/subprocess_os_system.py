"""
run an external command without interacting with it in the same
way as `os.system()`, use the `run()` function
"""

import subprocess as sp

completed = sp.run(['ls', '-l'])
print('returncode:', completed.returncode)
