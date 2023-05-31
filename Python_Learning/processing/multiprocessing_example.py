import time
import random
import os


from multiprocessing import Process, Queue, Pool, cpu_count, current_process


q = Queue()


def hello(n, q):
    q.put(os.getpid())
    random_int = random.randint(1, 3)
    time.sleep(random_int)
    print("Hello {}, I paused for {} sec\n".format(n, random_int))


if __name__ == "__main__":
    start_time = time.time()
    processes_list = []
    for i in range(10):
        p = Process(target=hello, args=(i, q))
        processes_list.append(p)
        p.start()

    for p in processes_list:
        p.join()

    end_time = time.time()
    print("Done in {} sec!".format(end_time-start_time))

    my_list = []
    while not q.empty():
        my_list.append(q.get())

    print(my_list)