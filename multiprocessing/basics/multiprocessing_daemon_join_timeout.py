import multiprocessing
import time
import sys


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
    n.start()

    d.join(1)
    print('d.is_alive()', d.is_alive())
    n.join()

    print('Exiting main')
    sys.stdout.flush()

# Since the timeout passed is less than the amount of time the daemon sleeps,
# the process is still “alive” after join() returns.

