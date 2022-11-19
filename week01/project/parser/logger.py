"""
Formats loggging messages and saves to web server. 
"""
from flask import Flask, render_template, request, url_for, redirect
import logging, os
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

file_handler = RotatingFileHandler('/files/parser-messages.log',
                                    maxBytes=16384,
                                    backupCount=20)
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in function %(funcName)s filename:%(filename)s:%(lineno)d]')
file_handler.setFormatter(file_formatter)
app.logger.addHandler(file_handler)