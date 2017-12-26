import multiprocessing
import time
import sys

"""
By default, main program will NOT exit until all children have exited.
Setting daemon, we can start a background process that runs without blocking the main
program from exiting.
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
    print('Exiting main')
    sys.stdout.flush()


"""
The output does not include the “Exiting” message from the daemon process, since all of the non-daemon processes (including the main program) exit before the daemon process wakes up from its two second sleep.

The daemon process is terminated automatically before the main program exits, which avoids leaving orphaned processes running.
"""
