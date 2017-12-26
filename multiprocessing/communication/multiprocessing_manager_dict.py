import multiprocessing
"""
By creating the list through the manager, it is shared and updates are
seen in all processes. Dictionaries are also supported.
"""


def worker(d, key, value):
    d[key] = value


def main():
    mgr = multiprocessing.Manager()
    d = mgr.dict()
    jobs = [
        multiprocessing.Process(target=worker, args=(d, i, i * 2))
        for i in range(10)
    ]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print('Result:', d)


if __name__ == '__main__':
    main()
