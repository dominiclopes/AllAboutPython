import multiprocessing
import sys
import time
import logging
from logging.handlers import QueueHandler, QueueListener
from queue import Queue

#
# class a(object):
#     def print_again(self):
#         logging.info("Inner Function")
#
#     def temp_func(self):
#         logging.info("Outer Function")
#         self.print_again()
#         time.sleep(2)


def run_fun_using_mp(logger, queue):
    logger.setLevel(logging.INFO)

    # Create a queue handler
    queue_handler = logging.handlers.QueueHandler(queue)
    queue_handler.setLevel(logging.INFO)
    # queue_handler.setFormatter(formatter_for_queue)
    # Adding the queue handler to the logger
    logger.addHandler(queue_handler)



    # format = "[%(asctime)s.%(msecs)03d][%(levelname)s][%(module)s] %(message)s"
    # date_format = "%d-%m-%Y %I:%M:%S"
    # logging.basicConfig(format=format, datefmt=date_format, level=logging.INFO,  stream=sys.stdout)
    # logging.info("Hello in executing run_fun_using_mp")

    # class_obj = a()
    logger.info("Logger level no is {},  name is {}")
    # for i in range(3):
    #     logging.info("Executing for {} time".format(i))
    #     class_obj.temp_func()
    # logging.info("I'm done here")






if __name__ == "__main__":
    formatter = logging.Formatter(fmt="[STREAM HANDLER][%(asctime)s.%(msecs)d][%(name)s][%(levelname)s]"
                                      "[processName:%(processName)s][threadName:%(threadName)s]"
                                      "[module:%(module)s] %(message)s", datefmt="%d-%m-%Y, %I:%M:%S")
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    # Create a stream handler for the logger
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    stream_handler.setStream(sys.stdout)
    # Add the stream handler to the logger
    root.addHandler(stream_handler)
    # Check if the stream handler is working as expected
    root.info("Checking if the stream handler is actually working")

    # Create a queue for the queue handler
    queue_for_queue_handler = multiprocessing.Queue()

    # Create a queue listener
    queue_listener = logging.handlers.QueueListener(queue_for_queue_handler)

    # Start the queue listener
    queue_listener.start()

    # Write code here
    root.info("Info level log message from the main")

    # Executing function using mp
    p1 = multiprocessing.Process(target=run_fun_using_mp, args=(root, queue_for_queue_handler,))
    p2 = multiprocessing.Process(target=run_fun_using_mp, args=(root, queue_for_queue_handler,))
    root.info("Lets start the Magic")
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    root.info("Magic has ended")

    # Stop the queue listener
    queue_listener.stop()
