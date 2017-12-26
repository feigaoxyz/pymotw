import multiprocessing
import time


def worker():
    name = multiprocessing.current_process().name
    print(name, 'starting')
    time.sleep(2)
    print(name, 'exiting')


def my_service():
    name = multiprocessing.current_process().name
    print(name, 'starting')
    time.sleep(3)
    print(name, 'exiting')


if __name__ == '__main__':
    service = multiprocessing.Process(
            name='my_service',
            target=my_service,
            )
    worker_1 = multiprocessing.Process(
            name='worker_1',
            target=worker
            )
    worker_2 = multiprocessing.Process(
            target=worker
            )

    worker_1.start()
    worker_2.start()
    service.start()

