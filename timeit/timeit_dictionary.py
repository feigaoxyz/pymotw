import timeit
import textwrap


range_size = 1000
count = 1000
setup_statement = ';'.join([
    "l = [(str(x), x) for x in range(1000)]",
    "d = {}",
    ])


def show_results(result):
    global count, range_size
    per_pass = 1000_000 * (result / count)
    print('{:6.2f} usec/pass'.format(per_pass), end=' ')
    per_item = per_pass / range_size
    print('{:6.2f} usec/item'.format(per_item))


print(f'{range_size} items')
print(f'{count} iterations')


print('__setitem__:', end=' ')
t = timeit.Timer(
        textwrap.dedent(
            """
            for s, i in l:
                d[s] = i
            """),
        setup_statement,
        )
show_results(t.timeit(number=count))


print('setdefault:', end=' ')
t = timeit.Timer(
        textwrap.dedent(
            """
            for s, i in l:
                d.setdefault(s, i)
            """),
        setup_statement,
        )
show_results(t.timeit(number=count))


print('KeyError:', end=' ')
t = timeit.Timer(
        textwrap.dedent(
            """
            for s, i in l:
                try:
                    existing = d[s]
                except KeyError:
                    d[s] = i
            """),
        setup_statement,
        )
show_results(t.timeit(number=count))


print('"not in":', end=' ')
t = timeit.Timer(
    textwrap.dedent(
        """
        for s, i in l:
            if s not in d:
                d[s] = i
        """),
    setup_statement
    )
show_results(t.timeit(number=count))

