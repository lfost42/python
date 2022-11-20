"""
Configuration variables
"""
import os
from flask import Flask

base_dir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'app.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False
ARCHIVED_FOLDER = '/files/archived'
ERROR_FOLDER = 'files/error/'