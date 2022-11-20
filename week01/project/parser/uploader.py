import os
import datetime
from shutil import move
import openpyxl
from flask import Flask

app = Flask(__name__)

def check_file(file):
    """check if file is expedia_report_summary

    Returns:
        _type_: _description_
    """
    if file.filename.startswith('expedia_report_monthly_'):
        archive_file(file)
        app.logger.info(f'{file} moved to archived')
    else:
        error_file(file)
        app.logger.error(f'{file} moved to error, file name does not start with expedia_report_monthly_')

def read_file(file):
    """_summary_

    Args:
        file (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        if not file:
            print('No file found with name: expedia_report_monthly_MONTH_YEAR.xlsx')
        else:
            try:
                workbook = openpyxl.load_workbook(file)
                return workbook
            except:
                app.logger.error('Data uanble to load')

    except:
        app.logger.error('Error reading File')

def archive_file(file):
    """Move to archived folder

    Args:
        file (_type_): FileStorage
    """
    arch_folder = 'files/archived'
    if os.path.exists(arch_folder):
        file.save(os.path.join(arch_folder, file.filename))

def error_file(file):
    """Move to error folder

    Args:
        file (_type_): FileStorage
    """
    err_folder = 'files/error/'
    if os.path.exists(err_folder):
        file.save(os.path.join(err_folder, file.filename))

def find_row(worksheet, search):
    """_summary_

    Args:
        worksheet (_type_): _description_
        search (_type_): _description_

    Returns:
        _type_: _description_
    """
    for x in range(1, worksheet.max_column + 1):
        for y in range(1, worksheet.max_row + 1):
            current_cell = worksheet.cell(row = y, column = x).value
            if isinstance(current_cell, str) and isinstance(search, str):
                if search in current_cell:
                    return y
            elif isinstance(current_cell, datetime.date) and isinstance(search, datetime.datetime):
                if current_cell.year == search.year and current_cell.month == search.month:
                    return y
            else:
                continue
    app.logger.error('Row with matching date not found')

def find_column(worksheet, name):
    """_summary_

    Args:
        worksheet (_type_): _description_
        name (_type_): _description_

    Returns:
        _type_: _description_
    """
    for x in range(1, worksheet.max_column + 1):
        for y in range(1, worksheet.max_row + 1):
            if worksheet.cell(row = y, column = x).value == name:
                return x
    app.logger.error('Column with matching date not found')