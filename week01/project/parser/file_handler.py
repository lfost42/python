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
    """Check if file type is excel, if name is long enough to 
    parse and whether it is a duplicate.

    Args:
        file (FileStorage): file for upload
    """
    extension = os.path.splitext(file.filename)[1].lower()
    if extension != '.xlsx':
        app.logger.error(f'File name: {file.filename} is not an excel file')
        return 'incorrect filetype'
    if len(file.filename) < 12: #  minimum 12 characters month:3 year:4 exten:5
        app.logger.error(f'File name: {file.filename} is too short.')
        return 'file name too short'
    path = f'files/archived/{file.filename}'
    if os.path.exists(path):
        app.logger.error(f'{file.filename} duplicate file | check_file')
        return 'duplicate file'
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
    except Exception as error:
        app.logger.exception(f'Data uanble to load: {error} | read_file')
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
        return 1
    app.logger.error(f'{arch_folder} does not exist.')
    return -1

def error_file(file):
    """Move to error folder

    Args:
        file (FileStorage): file for upload
    """
    err_folder = 'files/error/'

    if os.path.exists(err_folder):
        app.logger.info(f'{file} moved to error folder.')
        file.save(os.path.join(err_folder, file.filename))
        return 1
    app.logger.error(f'{err_folder} does not exist.')
    return -1

