import logging

logger = ""
if __name__ == "__main__":
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

logger.info("Im a INFO msg from file1")


class File1_class(object):
    def file1_func(self):
        logger.info("Im a file1 func msg")


a = File1_class()
a.file1_func()