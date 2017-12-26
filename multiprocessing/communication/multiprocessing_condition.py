import multiprocessing
import time

# Condition objects can be used to synchronize parts of a workflow so
# that some run in parallel but others run sequentially, even if they
# are in separate processes.


def stage_1(cond):
    """Perform first stage of work, then notify stage_2 to continue
    """
    name = multiprocessing.current_process().name
    print('Starting', name)
    with cond:
        print('{} done and ready for stage 2'.format(name))
        cond.notify_all()


def stage_2(cond):
    """Wait for the condition telling us stage_1 is done
    """
    name = multiprocessing.current_process().name
    print('Starting', name)
    with cond:
        cond.wait()
        print(f'{name} running')


def main():
    condition = multiprocessing.Condition()
    s1 = multiprocessing.Process(name='s1', target=stage_1, args=(condition, ))
    s2_clients = [
        multiprocessing.Process(
            name='stage_2[{}]'.format(i),
            target=stage_2,
            args=(condition, ),
        ) for i in range(3)
    ]
    for c in s2_clients:
        c.start()
        time.sleep(1)
    s1.start()

    s1.join()
    for c in s2_clients:
        c.join()


if __name__ == '__main__':
    main()
