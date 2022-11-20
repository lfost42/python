from flask import Blueprint, render_template
import logging, os
from logging.handlers import RotatingFileHandler
from flask import Flask

errors = Blueprint('errors', __name__)
app = Flask(__name__)

file_handler = RotatingFileHandler('files/expedia-info.log',
                                    maxBytes=16384,
                                    backupCount=20)
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in function %(funcName)s filename:%(filename)s:%(lineno)d]')
file_handler.setFormatter(file_formatter)
app.logger.addHandler(file_handler)

@errors.app_errorhandler(404)
def error_404(error):
    """
    returns 404.html error
    """
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(403)
def error_403(error):
    """
    returns 403.html error
    """
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(500)
def error_500(error):
    """
    returns 500.html error
    """
    return render_template('errors/500.html'), 500