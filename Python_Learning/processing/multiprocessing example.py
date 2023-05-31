from multiprocessing import Process, Queue, Lock, current_process, Pool
import multiprocessing


def sum_of_integers(input_list, queue):
    sum_of_values = sum(input_list)
    print("Sum of values in {} is {} on process {}".format(input_list, sum_of_values, current_process().name))
    queue.put(sum_of_values)


if __name__ == "__main__":
    print("Number of core: {}".format(multiprocessing.cpu_count()))
    q = Queue()

    p1 = Process(target=sum_of_integers, args=([1, 2, 3, 4, 5, 6, 7, 8, 9], q))
    p2 = Process(target=sum_of_integers, args=([2, 3, 4, 7, 6, 5, 9, 7, 6, 4, 1, 2, 3, 4], q))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    aha = (([1,2,3],q), ([4,5,6],q))
    p = Pool(4)
    p.map(sum_of_integers, aha)

    total = 0
    while not q.empty():
        total += q.get()
    print("Total = {}".format(total))
