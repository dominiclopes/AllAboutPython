import multiprocessing
import sys
import time
import logging
import random
from logging.handlers import QueueHandler, QueueListener
from queue import Queue


class a(object):

    def print_again(self):
        logging.info("Inner Function\n")

    def temp_func(self):
        logging.info("Outer Function")
        self.print_again()
        a = [1,2,3,4]
        time.sleep(random.choice(a))

def set_up_basic_conf():
    # Setting up the basic configuration
    format = "[%(process)d] [%(processName)s] [%(thread)d] [%(threadName)s] " \
             "[%(filename)s] [%(levelname)-8s] [%(name)s] [%(funcName)s] " \
             "%(message)s "
    datefmt = "%d-%m-%Y %I:%M:%S"
    logging.basicConfig(level=logging.DEBUG, format=format, datefmt=datefmt, stream=sys.stdout)
    # logging.basicConfig(filename="abc.txt", filemode='a', level=logging.DEBUG, format=format, datefmt=datefmt)

    logging.info("The basic configuration is setting")


def run_fun_using_mp():
    set_up_basic_conf()
    logging.info("Running this in multiprocessing")

    # logger.setLevel(logging.DEBUG)
    #
    # # Creating a queue handler
    # queue_handler = QueueHandler(queue)
    # # queue_handler.setLevel(logging.DEBUG)
    # logger.addHandler(queue_handler)
    # logger.info("Queue Handler level is {}".format(queue_handler.level))
    #
    # # Create a stream handler for queue
    # stream_handler_for_qh = logging.StreamHandler()
    # # stream_handler_for_qh.setLevel(logging.DEBUG)
    # # stream_handler_for_qh.setStream(sys.stdout)
    # stream_handler_for_qh.setFormatter(formatter)
    # logger.info("Stream Handler level is {}".format(stream_handler_for_qh.level))
    #
    #
    # # Creating queue listener
    # queue_listener = QueueListener(queue, stream_handler_for_qh)
    # queue_listener.start()
    #
    class_obj = a()
    for i in range(3):
        logging.info("Executing for {} time".format(i))
        class_obj.temp_func()
    logging.info("I'm done here")
    #
    # # Stopping queue listener and removing queue handler
    # queue_listener.stop()
    # logger.removeHandler(queue_handler)



if __name__ == "__main__":
    set_up_basic_conf()

    logging.info("The basic configuration is set")

    #
    # # Creating a queue
    # queue = multiprocessing.Queue()
    #
    # Executing function using mp
    p1 = multiprocessing.Process(target=run_fun_using_mp, args=())
    p2 = multiprocessing.Process(target=run_fun_using_mp, args=())
    p1.start()
    p2.start()
    p1.join()
    p2.join()





    """
     # Creating a logger
    logger = logging.getLogger("DOMINIC")
    logger.setLevel(logging.DEBUG)

    # Creating a formatter for file handler
    formatter = logging.Formatter(fmt="[%(asctime)s.%(msecs)03d][%(levelname)s][%(name)s][%(module)s] %(message)s",
                                  datefmt="%d-%m-%Y %I:%M:%S")
    # Creating a file handler
    file_handler = logging.FileHandler(filename="file_handler_log.txt", encoding="UTF-8", mode='a')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info("I will be printed in a file.")"""