"""
Logging handler.
"""
from flask import Flask
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

file_handler = RotatingFileHandler('files/expedia-info.log',
                                    maxBytes=16384,
                                    backupCount=20)
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in function %(funcName)s filename:%(filename)s:%(lineno)d]')
file_handler.setFormatter(file_formatter)
app.logger.addHandler(file_handler)
