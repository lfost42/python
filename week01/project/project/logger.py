"""
Takes all logged messages and saves it to files/messages.log
"""
from flask import Flask
from logging.handlers import RotatingFileHandler
import logging

app = Flask(__name__)

file_handler = RotatingFileHandler('/files/messages.log',
                                   maxBytes=16384,
                                   backupCount=20)
file_formatter = logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in function %(funcName)s filename:%(filename)s:%(lineno)d]')
file_handler.setFormatter(file_formatter)
app.logger.addHandler(file_handler)
