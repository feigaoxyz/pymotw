# signals and threads do not generally mix well

import signal
import threading
import os
import time


def signal_handler(num, stack):
    print('Received signal {} in {}'.format(num,
                                            threading.currentThread().name))


signal.signal(signal.SIGUSR1, signal_handler)


def wait_for_signal():
    print('Waiting for signal in', threading.currentThread().name)
    signal.pause()
    print('Done waiting')


# start a thread that will not receive the signal
receiver = threading.Thread(target=wait_for_signal, name='receiver')
receiver.start()
time.sleep(0.1)


def send_signal():
    print('Sending signal in', threading.currentThread().name)
    os.kill(os.getpid(), signal.SIGUSR1)


sender = threading.Thread(target=send_signal, name='sender')
sender.start()
sender.join()

# wait for the thread to see the signal (NOT going to happen!)
print('Waiting for', receiver.name)
signal.alarm(2)
receiver.join()
