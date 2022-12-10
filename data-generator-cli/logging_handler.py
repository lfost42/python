"""
Logging console handler. 
"""
import logging

# Create a logger object
logger = logging.getLogger(__name__)

# Set the log level to DEBUG
logger.setLevel(logging.DEBUG)

# Create a handler for logging to the console
console_handler = logging.StreamHandler()

# Set the log level for the console handler to DEBUG
console_handler.setLevel(logging.DEBUG)

# Create a formatter for the log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set the formatter for the console handler
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)