import logging

# # CASE: Check the defaults
# # The default logging level is WARNING
# logging.critical("Logs a message with level CRITICAL on the root logger")
# logging.error("Logs a message with level ERROR on the root logger")
# logging.warning("Logs a message with level WARNING on the root logger")
# logging.info("Logs a message with level INFO on the root logger")
# logging.debug("Print a DEBUG level log")
# logging.exception("Exception: Logs a message with level ERROR on the root logger. "
#                   "This function should only be called from an exception handler? *Research* "
#                   "Exception info is added to the logging message. ")  # TODO


# # #####################################################################################################################
# # CASE
# # If NOTSET is used it does not print anything
# # TODO I do not understand its used
# logging.log(level=logging.CRITICAL, msg="Logs a message with level level on the root logger")


# # ####################################################################################################################
# # CASE: Setting the basic logger level
# # Once the logging level is set is cannot be changes in the middle of the program
# logging.basicConfig(level=logging.NOTSET)
# logging.critical("Logs a message with level CRITICAL")
# logging.error("Logs a message with level ERROR")
# logging.warning("Logs a message with level WARNING")
# logging.info("Logs a message with level INFO")
# logging.debug("Print a DEBUG level log")


# # #####################################################################################################################
# # CASE: Playing around with the basic logger
# # Learning about how to set the stream and file handler using the basic configuration.
# # Learning to set the logging level, logging format, date format)
# # Learning to stream the logs
# import sys
# level = logging.INFO
# format = "[%(asctime)s] [%(created)f] [%(filename)s] [%(funcName)s] [%(levelname)-8s] [%(levelno)s] [%(lineno)d]" \
#          " [%(message)-34s] [%(module)s] [%(name)s] [%(pathname)s] [%(process)d] [%(processName)s] [%(relativeCreated)d]" \
#          " [%(thread)d] [%(threadName)s]"
# datefmt = "%d-%m-%Y %I:%M:%S"
# logging.basicConfig(stream=sys.stdout, level=level, format=format, datefmt=datefmt)
# logging.critical("Logs a message with level CRITICAL")
# logging.error("Logs a message with level ERROR")
# logging.warning("Logs a message with level WARNING")
# logging.info("Logs a message with level INFO")
# logging.exception("Exception: Logs a message with level ERROR on the root logger.")


# # #####################################################################################################################
# # CASE: Playing around with the basic logger handlers
# # Learning about how to set the stream and file handler using the basic configuration.
# # Learning to set the logging level, logging format, date format)
# # Learning to stream the logs
# import sys
# level = logging.INFO
# format = "[%(asctime)s] [%(created)f] [%(filename)s] [%(funcName)s] [%(levelname)-8s] [%(levelno)s] [%(lineno)d]" \
#          " [%(message)-34s] [%(module)s] [%(name)s] [%(pathname)s] [%(process)d] [%(processName)s] [%(relativeCreated)d]" \
#          " [%(thread)d] [%(threadName)s]"
# datefmt = "%d-%m-%Y %I:%M:%S"
# formatter = logging.Formatter(fmt=format, datefmt=datefmt)
#
#
# logger = logging.getLogger("TestReporter")
# # logger.setLevel(logging.INFO)
#
# stream_handler = logging.StreamHandler()
# stream_handler.setLevel(logging.INFO)
# stream_handler.setStream(stream=sys.stdout)
# stream_handler.setFormatter(fmt=formatter)
# logger.addHandler(stream_handler)
#
# logger.critical("Logs a message with level CRITICAL")
# logger.error("Logs a message with level ERROR")
# logger.warning("Logs a message with level WARNING")
# logger.info("Logs a message with level INFO")
# logger.exception("Exception: Logs a message with level ERROR on the root logger.")


# #####################################################################################################################
# CASE:
import logging
import logging.handlers
import sys
import multiprocessing
import time
from multiprocessing import Process

def temp_func(queue, logger):
    logger.setLevel(logging.DEBUG)
    format = "[%(asctime)s] [%(funcName)s] [%(levelname)-8s] [%(message)-34s] [%(name)s] [%(pathname)s] " \
             "[%(processName)s] [%(thread)d] [%(threadName)s]"
    datefmt = "%d-%m-%Y %I:%M:%S"
    formatter = logging.Formatter(fmt=format, datefmt=datefmt)

    # Creating a Queue, A queue handler and adding the queue handler to the logger
    queue_handler = logging.handlers.QueueHandler(queue)
    # queue_handler.setLevel(logging.DEBUG)
    # queue_handler.setFormatter(formatter)
    logger.addHandler(queue_handler)

    # Creating a stream handler for the queue handler
    stream_handler_for_queue_handler = logging.StreamHandler()
    stream_handler_for_queue_handler.setStream(stream=sys.stdout)
    stream_handler_for_queue_handler.setLevel(level=logging.DEBUG)
    stream_handler_for_queue_handler.setFormatter(fmt=formatter)

    # Creating a Queue Listener
    queue_listener = logging.handlers.QueueListener(queue, stream_handler_for_queue_handler, respect_handler_level=True)
    queue_listener.start()
    logger.info("Well I just will keep printing messages")

    logger.warning("Inside the queue.    hoo I'm a warning   ")
    time.sleep(3)
    logger.warning("Inside the queue. I'm a warning level log")
    logger.info("Well I just will keep printing messages")

    queue_listener.stop()
    logger.removeHandler(queue_handler)

if __name__ == "__main__":
    level = logging.INFO
    format = "[%(asctime)s] [%(funcName)-9s] [%(levelname)-8s] [%(message)-41s] [%(name)s] [%(pathname)s] " \
             "[%(processName)s] [%(thread)d] [%(threadName)s]"
    datefmt = "%d-%m-%Y %I:%M:%S"
    formatter = logging.Formatter(fmt=format, datefmt=datefmt)

    logger = logging.getLogger("TestReporter")
    logger.setLevel(logging.DEBUG)


    stream_handler = logging.StreamHandler()
    stream_handler.setStream(stream=sys.stdout)
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(fmt=formatter)
    logger.addHandler(stream_handler)
    logger.info("I'm a INFO level   log")

    queue = multiprocessing.Queue()

    p1 = Process(target=temp_func, args=(queue, logger))
    p2 = Process(target=temp_func, args=(queue, logger))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
