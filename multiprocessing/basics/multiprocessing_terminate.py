import multiprocessing
import time


def slow_worker():
    print('staring worker')
    time.sleep(3)
    print('finished worker')


if __name__ == '__main__':
    p = multiprocessing.Process(
            target=slow_worker,
            )
    print('before:', p, p.is_alive())

    p.start()
    print('started:', p, p.is_alive())

    p.terminate()
    print('terminated:', p, p.is_alive())

    p.join()
    print('joined:', p, p.is_alive())

