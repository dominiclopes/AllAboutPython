import logging.handlers
import queue
import sys

# Create a logger instance
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# Create formatter for the handler
formatter_for_stream = logging.Formatter(fmt="[STREAM HANDLER][%(asctime)s.%(msecs)d][%(name)s][%(levelname)s]"
                                            "[processName:%(processName)s][threadName:%(threadName)s]"
                                            "[module:%(module)s] %(message)s", datefmt="%d %b %Y, %I:%M:%S")

formatter_for_queue = logging.Formatter(fmt="[QUEUE HANDLER][%(asctime)s.%(msecs)d][%(name)s][%(levelname)s]"
                                            "[processName:%(processName)s][threadName:%(threadName)s]"
                                            "[module:%(module)s] %(message)s", datefmt="%d %b %Y, %I:%M:%S")

# Create a stream handler for the logger
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter_for_stream)
stream_handler.setStream(sys.stdout)
# Add the stream handler to the logger
root_logger.addHandler(stream_handler)

# Check if the stream handler is working as expected
root_logger.info("Checking if the stream handler is actually working")

# Create a queue for the queue handler
queue_for_queue_handler = queue.Queue()

# Create a queue handler
queue_handler = logging.handlers.QueueHandler(queue_for_queue_handler)
queue_handler.setLevel(logging.INFO)
queue_handler.setFormatter(formatter_for_queue)
# Adding the queue handler to the logger
root_logger.addHandler(queue_handler)

# Create a queue listener
queue_listener = logging.handlers.QueueListener(queue_for_queue_handler, stream_handler,respect_handler_level=True)

# Start the queue listener
queue_listener.start()

# Write code here
root_logger.info("Info level log message")

# Stop the queue listener
queue_listener.stop()

# Remove the queue handler from the logger
root_logger.removeHandler(queue_handler)
