import subprocess
"""
Multiple commands can be connected into a pipeline, similar to the way
the Unix shell works, by creating separate Popen instances and chaining
their inputs and outputs together.
"""

cat = subprocess.Popen(
    ['ls', '-l'],
    stdout=subprocess.PIPE,
)

grep = subprocess.Popen(
    ['grep', 'py'],
    stdin=cat.stdout,
    stdout=subprocess.PIPE,
)

cut = subprocess.Popen(
    ['cut', '-f', '12', "-d "],
    stdin=grep.stdout,
    stdout=subprocess.PIPE,
)

end_of_pipe = cut.stdout

print('Python files:')
for line in end_of_pipe:
    print(line.decode('utf-8').strip())
