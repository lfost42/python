"""
Parses date from file name.
"""
import re
from file_handler import error_file
from logging_handler import app

def check_year(file):
    """Parses file name for a 4 digit number and if found, returns the last
    2 digits to represent the year.

    Args:
        file (string): Name of excel file.

    Returns:
        string: The last 2 digits in the parsed 4 digit number.
    """
    filename = file.filename
    year = re.findall('[0-9]+', filename)

    if (not year or len(year[0]) != 4):
        error_file(file)
        app.logger.error(f'Could not extract {year} | check_year')
        return -1

    app.logger.info('Year successfully parsed form file name.')
    return year[0][-2:]

def check_month(file):
    """Parses file name for 3 letter month code.

    Args:
        file (string): Name of the file.

    Returns:
        string: 3 letter month code parsed from file name.
        integer: -1 if month could not be extracted.
    """
    filename = file.filename.lower()
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    for month in months:
        if month in filename:
            app.logger.info(f'Month successfully parsed from {file}.')
            return month
    app.logger.error(f'ERROR: unable to extract month from {file}| check_month')
    return -1

def get_date(file):
    """Invokes the check_year and check_month methods to create a date list.

    Args:
        file (string): Name of file.

    Returns:
        list: List with year at index 0 and month at index 1.
    """
    year = check_year(file)
    month = check_month(file)

    if -1 in (year,month):
        app.logger.error(
            f'Could not parse date month: {month} year: {year} from {file.filename}')
        return -1

    app.logger.info(f'Date generated from {file}')
    return [year, month]
