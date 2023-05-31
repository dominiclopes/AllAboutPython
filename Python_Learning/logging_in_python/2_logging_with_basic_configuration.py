import logging

# Setting up the basic configuration
# The configuration is set only once throughout the program
import sys

format = "[%(asctime)s] [%(created)f] [%(filename)s] [%(funcName)s] [%(levelname)-8s] [%(levelno)s] [%(lineno)d]" \
         " [%(message)-34s] [%(module)s] [%(name)s] [%(pathname)s] [%(process)d] [%(processName)s] [%(relativeCreated)d]" \
         " [%(thread)d] [%(threadName)s]"
datefmt = "%d-%m-%Y %I:%M:%S"
logging.basicConfig(level=logging.DEBUG, format=format, datefmt=datefmt, stream=sys.stderr)


logging.critical("critical level log message")

try:
    raise Exception("I generated this error")
except Exception:
    logging.error("error level log message without exception info", exc_info=False)
    logging.error("error level log message with exception info", exc_info=True)

logging.warning("warning level log message")
logging.info("info level log message")
logging.debug("debug level log message")