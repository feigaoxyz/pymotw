# textwrap_example.py

sample_text = '''  
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''

print('ORIGINAL:', '-'*20)
for line in sample_text.splitlines():
    print('{:2d}|{}'.format(len(line), line))
# print(sample_text)
print('-' * 30)

if __name__ == '__main__':
    print(sample_text)
