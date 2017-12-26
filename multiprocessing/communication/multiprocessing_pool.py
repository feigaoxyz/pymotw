import multiprocessing
"""
The Pool class can be used to manage a fixed number of workers for simple
cases where the work to be done can be broken up and distributed between
workers independently. The return values from the jobs are collected and
returned as a list.
"""


def do_calculation(data):
    return data * 2


def start_process():
    print('Starting', multiprocessing.current_process().name)


def main():
    inputs = list(range(10))
    print('Input:', inputs)

    builtin_outputs = map(do_calculation, inputs)
    print('Built-in:', list(builtin_outputs))

    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(
        processes=pool_size,
        initializer=start_process,
    )
    pool_outputs = pool.map(do_calculation, inputs)
    pool.close()
    pool.join()
    print('Pool:', pool_outputs)


if __name__ == '__main__':
    main()
