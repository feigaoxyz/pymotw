import signal
import os


def do_exit(sig, stack):
    raise SystemExit('Exiting')


signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGUSR1, do_exit)

print('PID:', os.getpid())

# waiting for a signal
signal.pause()

# use `kill -USR1 $pid` to stop program
