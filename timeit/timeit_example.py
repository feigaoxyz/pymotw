import timeit

t = timeit.Timer(
        "print('main statement')",  # main
        "print('setup env')",  # setup
        )

print('timeit:')
print(t.timeit(2))

print('repeat:')
print(t.repeat(3, 2))

