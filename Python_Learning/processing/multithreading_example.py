import time
import random


from threading import Thread


def hello(n):
    random_int = random.randint(1, 3)
    time.sleep(random_int)
    print("Hello {}, I paused for {} sec\n".format(n, random_int))


if __name__ == "__main__":
    start_time = time.time()

    threads_list = []
    for i in range(10):
        t = Thread(target=hello, args=(i,))
        threads_list.append(t)
        t.start()

    for t in threads_list:
        t.join()

    end_time = time.time()
    print("Done in {} sec!".format(end_time - start_time))
