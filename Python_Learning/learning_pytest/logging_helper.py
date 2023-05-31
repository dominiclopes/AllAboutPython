import logging
import sys


class Logger(object):

    def __init__(self):
        # Get logger object
        self.report_logger = logging.getLogger(__name__)

        # Creating a formatter
        log_format = "[%(asctime)s.%(msecs)03d][%(levelname)s][%(module)s][logger_name:%(name)s][%(processName)s] " \
                     "[%(thread)d] [%(threadName)s] %(message)s"
        date_format = "%d-%m-%y %H:%M:%S"
        formatter = logging.Formatter(fmt=log_format, datefmt=date_format)

        # # Create a Stream handler for the logger
        # stream_handler = logging.StreamHandler()
        # stream_handler.setLevel(logging.INFO)
        # # stream_handler.setStream(sys.stdout)
        # stream_handler.setFormatter(formatter)

        # # Creating file handler
        # file_handler = logging.FileHandler("report_logger.log")
        # file_handler.setLevel(logging.INFO)
        # file_handler.setFormatter(formatter)

        # # Add the handlers to the logger
        # self.report_logger.addHandler(stream_handler)
        # self.report_logger.addHandler(file_handler)


        self.report_logger.info("Initialized the logger")
