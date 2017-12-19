# although alarms can be set in any thread, they are always
# received by the main thread.

import signal
import time
import threading


def signal_handler(num, stack):
    print('Alarm in', threading.currentThread().name, time.ctime())


signal.signal(signal.SIGALRM, signal_handler)


def use_alarm():
    t_name = threading.currentThread().name
    print('Setting alarm in', t_name, time.ctime())
    signal.alarm(1)
    print('Sleeping in', t_name, time.ctime())
    time.sleep(3)
    print('Done with sleep in', t_name, time.ctime())


# start a thread that will not receive the signal
alarm_thread = threading.Thread(
    target=use_alarm,
    name='alarm_thread',
)
alarm_thread.start()
time.sleep(0.1)

# wait for the thread to see the signal (NOT happening)
print('Waiting for', alarm_thread.name, time.ctime())
alarm_thread.join()

print('Exiting normally', time.ctime())
