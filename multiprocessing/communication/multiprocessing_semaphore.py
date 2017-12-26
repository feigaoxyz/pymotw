import random
import multiprocessing
import time
"""
Sometimes it is useful to allow more than one worker access to a resource
at a time, while still limiting the overall number. A Semaphore is one
way to manage those connections.

The list of active processes is maintained centrally in the ActivePool
instance via a special type of list object created by a Manager. The
Manager is responsible for coordinating shared information state between
all of its users.
"""


class ActivePool:
    def __init__(self):
        super(ActivePool, self).__init__()
        self.mgr = multiprocessing.Manager()
        self.active = self.mgr.list()
        self.lock = multiprocessing.Lock()

    def make_active(self, name):
        with self.lock:
            self.active.append(name)

    def make_inactive(self, name):
        with self.lock:
            self.active.remove(name)

    def __str__(self):
        with self.lock:
            return str(self.active)


def worker(s, pool):
    name = multiprocessing.current_process().name
    with s:
        pool.make_active(name)
        print(f'Activating {name} now running {pool}')
        time.sleep(random.random())
        pool.make_inactive(name)


def main():
    pool = ActivePool()
    s = multiprocessing.Semaphore(3)
    jobs = [
        multiprocessing.Process(
            target=worker,
            name=str(i),
            args=(s, pool),
        ) for i in range(10)
    ]
    for j in jobs:
        j.start()

    while True:
        alive = 0
        for j in jobs:
            if j.is_alive():
                alive += 1
                j.join(timeout=0.1)
                print(f'Now running {pool}')
        if alive == 0:
            print('All done')
            break


if __name__ == '__main__':
    main()
