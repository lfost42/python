"""
Logging handler.
"""
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask.logging import create_logger

app = Flask(__name__, instance_relative_config=True)
app.logger = create_logger(app)

# Creates rotating file handler to limit files to 16384 bytes.
file_handler = RotatingFileHandler('files/expedia-info.log',
                                    maxBytes=16384,
                                    backupCount=20)

# Formats log files with data to include.
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: \
                                   %(message)s [in function %(funcName)s \
                                   filename:%(filename)s:%(lineno)d]')

file_handler.setFormatter(file_formatter)
app.logger.addHandler(file_handler)
