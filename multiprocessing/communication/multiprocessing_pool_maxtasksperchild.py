import multiprocessing
"""
By default, Pool creates a fixed number of worker processes and passes
jobs to them until there are no more jobs. Setting the maxtasksperchild
parameter tells the pool to restart a worker process after it has finished
a few tasks, preventing long-running workers from consuming ever more
system resources.
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

    pool_size = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(
        processes=pool_size,
        initializer=start_process,
        maxtasksperchild=2,
    )
    pool_outputs = pool.map(do_calculation, inputs)
    pool.close()
    pool.join()
    print('Pool:', pool_outputs)


if __name__ == '__main__':
    main()
