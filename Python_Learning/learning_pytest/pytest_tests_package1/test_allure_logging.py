import logging
import multiprocessing
import sys
import time

from logging.handlers import QueueHandler, QueueListener
from ..logging_helper import Logger

class a(object):
    def __init__(self, logger):
        self.report_logger = logger.report_logger

    def print_again(self):
        self.report_logger.info("Inner Function")

    def temp_func(self):
        self.report_logger.info("Outer Function")
        self.print_again()
        time.sleep(2)


def run_fun_using_mp(logger):
    logger.report_logger.setLevel(logging.INFO)
    # configuration
    format = "[%(asctime)s.%(msecs)03d][%(levelname)s][%(module)s] %(name)s [process:%(processName)s thread:%(thread)s threadname:%(threadName)s  ] %(message)s"
    date_format = "%d-%m-%Y %I:%M:%S"
    formatter = logging.Formatter(fmt=format, datefmt=date_format)

    # Create a queue for queue handler
    queue = multiprocessing.Queue()

    # Create a queue handler
    queue_handler = QueueHandler(queue)
    queue_handler.setLevel(logging.INFO)
    queue_handler.setFormatter(formatter)
    logger.report_logger.addHandler(queue_handler)

    # Create a handler for queue handler
    # stream_handler_foe_queue = logging.StreamHandler()
    # stream_handler_foe_queue.setLevel(logging.INFO)
    # stream_handler_foe_queue.setStream(sys.stdout)
    # stream_handler_foe_queue.setFormatter(formatter)

    # Create a queue listener
    queue_listener = QueueListener(queue)

    # start queue listener
    queue_listener.start()

    logger.report_logger.info("Hello in executing run_fun_using_mp")

    class_obj = a(logger)
    logging.info("Logger level no is {},  name is {}")
    for i in range(3):
        logger.report_logger.info("Executing for {} time".format(i))
        class_obj.temp_func()
    logger.report_logger.info("I'm done here")

    # Stop queue listener
    queue_listener.stop()

    # Remove queue_handler from logger
    logger.report_logger.removeHandler(queue_handler)


def test_timepass():
    logger = Logger()

    p1 = multiprocessing.Process(target=run_fun_using_mp, args=(logger,))
    p2 = multiprocessing.Process(target=run_fun_using_mp, args=(logger,))
    logger.report_logger.info("Lets start the Magic")
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    logger.report_logger.info("Magic has ended")

