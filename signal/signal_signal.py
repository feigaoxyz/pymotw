# signal_signal.py

import signal
import os
import time


def receive_signal(signum, stack):
    print('Received:', signum)


# register signal handlers
signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

# print pid
print('My PID is:', os.getpid())

while True:
    print('Waiting...')
    time.sleep(3)

# run `kill -USR1 $pid` in terminal
