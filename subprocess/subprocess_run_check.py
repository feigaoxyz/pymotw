"""
Passsing `check=True` equiv to `check_call()`
"""

import subprocess

try:
    subprocess.run(['false'], check=True)
except subprocess.CalledProcessError as err:
    print('Error:', err)
