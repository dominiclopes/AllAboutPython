from . file1 import File1_class
import logging

logger = logging.getLogger(__name__)
level = logging.INFO
format = "[%(asctime)s] [%(funcName)-9s] [%(levelname)-8s] [%(message)-41s] [%(name)s] [%(pathname)s] " \
         "[%(processName)s] [%(thread)d] [%(threadName)s]"
datefmt = "%d-%m-%Y %I:%M:%S"
formatter = logging.Formatter(fmt=format, datefmt=datefmt)

logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(fmt=formatter)
logger.addHandler(stream_handler)


logger.warning("Im a INFO msg from file2")

def file2_func():
    logger.warning("Im a file2 func msg")


file2_func()

a = File1_class()
a.file1_func()