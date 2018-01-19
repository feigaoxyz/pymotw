import textwrap
from textwrap_example import sample_text


def should_indent(line):
    print('Indent {!r}?'.format(line.strip()))
    print('Ints: ', [ord(c) for c in line])
    return len(line.strip()) % 2 == 0


dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
final = textwrap.indent(
        wrapped, 
        'EVEN ',
        predicate=should_indent
        )

print('\nQuoted blocks:\n')
print(final)

