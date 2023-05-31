import logging


logging.critical("critical level log message")
logging.warning("warning level log message")

try:
    raise Exception("I generated this error")
except Exception:
    logging.error("error level log message without exception info", exc_info=False)
    logging.error("error level log message with exception info", exc_info=True)
logging.info("info level log message")
logging.debug("debug level log message")