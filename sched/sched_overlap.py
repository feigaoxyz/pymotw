import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def long_event(name):
    print('begin event:', time.ctime(time.time()), name)
    time.sleep(2)
    print('finish event:', time.ctime(time.time()), name)

print('start:', time.ctime(time.time()))
scheduler.enter(2, 1, long_event, ('first', ))
scheduler.enter(3, 1, long_event, ('second', ))

scheduler.run()

