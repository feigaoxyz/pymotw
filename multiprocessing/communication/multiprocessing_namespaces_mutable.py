import multiprocessing
"""
It is important to know that updates to the contents of mutable values in
the namespace are not propagated automatically.
"""


def producer(ns, event):
    # DOES NOT UDPATE GLOBAL VALUE!
    ns.my_list.append('This is the value')
    event.set()


def consumer(ns, event):
    try:
        print('Before event: {}'.format(ns.my_list))
    except Exception as err:
        print('Before event, error:', str(err))
    event.wait()
    print('After event:', ns.my_list)


def main():
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()
    namespace.my_list = []

    event = multiprocessing.Event()
    p = multiprocessing.Process(target=producer, args=(namespace, event))
    c = multiprocessing.Process(target=consumer, args=(namespace, event))
    c.start()
    p.start()
    c.join()
    p.join()


if __name__ == '__main__':
    main()
