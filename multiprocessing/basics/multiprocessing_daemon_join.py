import multiprocessing
import time
import sys

"""
To wait until a process has completed its work and exited, use the join() method.

Since the main process waits for the daemon to exit using join(), the “Exiting” message is printed this time.
"""


def daemon():
    p = multiprocessing.current_process()
    print('Starting', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(2)
    print('Exiting', p.name, p.pid)
    sys.stdout.flush()


def non_daemon():
    p = multiprocessing.current_process()
    print('Starting', p.name, p.pid)
    sys.stdout.flush()
    print('Exiting', p.name, p.pid)
    sys.stdout.flush()


if __name__ == '__main__':
    d = multiprocessing.Process(
            name='daemon',
            target=daemon
            )
    d.daemon = True

    n = multiprocessing.Process(
            name='non-daemon',
            target=non_daemon
            )
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()
    time.sleep(0.2)

    d.join()
    n.join()

    print('Exiting main')
    sys.stdout.flush()

