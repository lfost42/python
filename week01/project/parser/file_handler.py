"""
Upload, read, and move excel files.
"""
import os
import os.path
from openpyxl import load_workbook
from logging_handler import app

def check_file(file):
    """Initial file check:
	1. extension is .xlsx because openpyxl will not open other file types.
	2. file name is at least 2 charachters which is the minimum required
		for parsing: 3 for month, 4 for year, and 5 for extension.
	3. checks if file is a duplicate.

    Args:
        file (FileStorage): file for upload
    Returns: string (brief error message that is passed to the web browser)
    or 1 if we detected no errors.
    """
    extension = os.path.splitext(file.filename)[1].lower()
    if extension != '.xlsx':
        app.logger.error(f'File name: {file.filename} is not an excel file')
        return 'incorrect filetype'
    if len(file.filename) < 12: # month:3 year:4 exten:5
        app.logger.error(f'File name: {file.filename} is too short.')
        return 'file name too short'
    path = f'files/archived/{file.filename}'
    if os.path.exists(path):
        app.logger.error(f'{file.filename} duplicate file | check_file')
        return 'duplicate file'
    app.logger.info('{file} checked, not a duplicate.')
    return 1

def read_file(file):
    """Reads file and raises an exception when the workbook cannot be loaded.

    Args:
        file (FileStorage): file for upload
    Returns: workbook if successful and -1 if not.
    """
    try:
        workbook = load_workbook(file, data_only=True)
        app.logger.info(f'{file} read.')
        return workbook
    except Exception as error:
        app.logger.exception(f'Data uanble to load: {error} | read_file')
        return -1

def archive_file(file):
    """Moves file to archived folder if archive folder is found, logs error
        if it cannot be found.
    Args:
        file (FileStorage): file for upload
    Returns(integer): returns 1 when successful and -1 if not.
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
