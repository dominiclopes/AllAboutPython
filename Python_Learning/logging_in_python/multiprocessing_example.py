import multiprocessing
import sys
import time
import logging
from logging.handlers import QueueHandler, QueueListener
from queue import Queue
from multiprocessing_logging import install_mp_handler


class a(object):
    def print_again(self):
        logging.info("Inner Function")

    def temp_func(self):
        logging.info("Outer Function")
        self.print_again()
        time.sleep(2)


def run_fun_using_mp():
    # log_format = 'mp %(asctime)s %(name)s %(levelname)-8s ' \
    #              '[process:%(processName)s thread:%(thread)s threadname:%(threadName)s] %(message)s'
    # date = "%d-%m-%Y %I:%M:%S"
    # logging.basicConfig(level=logging.INFO, format=log_format, datefmt=date)
    class_obj = a()
    logging.warning("Info level log message")
    for i in range(3):
        logging.info("Executing for {} time".format(i))
        class_obj.temp_func()
    logging.info("I'm done here")


if __name__ == "__main__":
    log_format = 'main %(asctime)s %(name)s %(levelname)-8s ' \
                 '[process:%(processName)s thread:%(thread)s threadname:%(threadName)s] %(message)s'
    date = "%d-%m-%Y %I:%M:%S"
    logging.basicConfig(level=logging.INFO, format=log_format, datefmt=date, stream=sys.stdout)

    logging.info("info level log message")


    # install_mp_handler()
    multiprocessing.log_to_stderr()
    # logger = multiprocessing.get_logger()
    # logger.setLevel(logging.INFO)

    # Executing function using mp
    p1 = multiprocessing.Process(target=run_fun_using_mp)
    p2 = multiprocessing.Process(target=run_fun_using_mp)
    p1.start()
    p2.start()

    p1.join()
    p2.join()
