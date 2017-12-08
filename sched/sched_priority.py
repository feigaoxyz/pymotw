import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def print_event(name):
    print('event:', time.ctime(time.time()), name)

now = time.time()
print('start:', time.ctime(now))

scheduler.enterabs(now + 2, 2, print_event, ('first',))
scheduler.enterabs(now + 2, 1, print_event, ('second',))

scheduler.run()

