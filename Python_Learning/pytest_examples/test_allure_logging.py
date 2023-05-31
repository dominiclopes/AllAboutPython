import multiprocessing
import sys
import time
import logging
from logging.handlers import QueueHandler, QueueListener
from queue import Queue


class a(object):
    def print_again(self):
        logging.info("Inner Function")

    def temp_func(self):
        logging.info("Outer Function")
        self.print_again()
        time.sleep(2)


def run_fun_using_mp():
    format = "[%(asctime)s.%(msecs)03d][%(levelname)s][%(module)s] %(message)s"
    date_format = "%d-%m-%Y %I:%M:%S"
    logging.basicConfig(level=logging.INFO)
    logging.info("Hello in executing run_fun_using_mp")

    class_obj = a()
    logging.info("Logger level no is {},  name is {}")
    for i in range(3):
        logging.info("Executing for {} time".format(i))
        class_obj.temp_func()
    logging.info("I'm done here")



def test_timepass():
    # Get logger object
    logger = logging.getLogger("TestLogger")

    # Creating a formatter
    log_format = "[(asctime)s.%(msecs)03d][%(levelname)s][%(module)s][%(name)s][%(processName)s] [%(thread)d] [%(threadName)s] %(message)s"
    date_format = "%d-%m-%y %H:%M:%S"
    formatter = logging.Formatter(fmt=log_format, datefmt=date_format)

    # Create a Stream handler for the logger
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setStream(sys.stdout)
    stream_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(stream_handler)

    logger.info("INFO level log message")
    print("Hello")
    # format = "[%(asctime)s.%(msecs)03d][%(levelname)s][%(module)s] %(message)s"
    # date_format = "%d-%m-%Y %I:%M:%S"
    # logging.basicConfig(format=format, datefmt=date_format, level=logging.INFO, stream=sys.stdout)

    # Executing function using mp
    # p1 = multiprocessing.Process(target=run_fun_using_mp)
    # p2 = multiprocessing.Process(target=run_fun_using_mp)
    # logging.info("Lets start the Magic")
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    # logging.info("Magic has ended")

