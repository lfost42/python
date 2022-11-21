"""
Upload, read, and move excel files.
"""
import os
import os.path
from openpyxl import load_workbook
from logging_handler import app
# import config as cfg

# cfg = app.config.from_pyfile('config.py', instance_relative_config=True)
# with app.open_instance_resource('application.cfg') as f:
#     config = f.read()

def check_file(file):
    """Check if file is a duplicate.

    Args:
        file (FileStorage): file for upload
    """
    path = f'files/archived/{file.filename}'

    if os.path.exists(path):
        app.logger.error(f'{file} duplicate file | check_file')
        return -1
    app.logger.info('{file} checked, not a duplicate.')
    return 1

def read_file(file):
    """Reads file

    Args:
        file (FileStorage): file for upload
    """
    try:
        workbook = load_workbook(file, data_only=True)
        app.logger.info(f'{file} read.')
        return workbook
    except ImportError as import_error:
        app.logger.exception(f'Data uanble to load: {import_error} | read_file')
        return -1

def archive_file(file):
    """Move to archived folder

    Args:
        file (FileStorage): file for upload
    """
    arch_folder = 'files/archived/'

    if os.path.exists(arch_folder):
        app.logger.info(f'{file} to archived folder.')
        file.save(os.path.join(arch_folder, file.filename))

def error_file(file):
    """Move to error folder

    Args:
        file (FileStorage): file for upload
    """
    err_folder = 'files/error/'

    if os.path.exists(err_folder):
        app.logger.info(f'{file} moved to error folder.')
        file.save(os.path.join(err_folder, file.filename))
