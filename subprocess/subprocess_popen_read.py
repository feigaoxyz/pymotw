import subprocess
"""
To run a process and read all of its output, set the stdout value
to PIPE and call communicate().
"""

print('read:')
proc = subprocess.Popen(['echo', '"to stdout"'], stdout=subprocess.PIPE)
stdout_value = proc.communicate()[0].decode('utf-8')
print('stdout:', repr(stdout_value))
