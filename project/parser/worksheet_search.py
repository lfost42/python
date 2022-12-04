"""
Searches excel worksheet to determine row and column coordinates.
"""
import datetime
from logging_handler import app

def find_row(worksheet, search):
    """Uses search term to find a column coordinate.

    Args:
        worksheet (FileStorage): The active worksheet in the excel file we are parsing.
        search (string): Search term required to lcoate a row.

    Returns:
        Integer: Coordinate for searched row.
    """
    for my_row in range(1, worksheet.max_row + 1):
        text = worksheet.cell(row = my_row, column = 1).value

        if text is not None:
            if isinstance(text, datetime.datetime):
                date_str = str(text.strftime("%b-%Y")).lower()
                new_txt = date_str[:4] + date_str[-2:]
                if new_txt == search:
                    app.logger.info(f'{search} found in {worksheet}.')
                    return my_row

            if isinstance(text, str):
                if search.lower() in text.lower():
                    app.logger.info(f'{search} found in {worksheet}.')
                    return my_row

    app.logger.error(f'{search} not found in {worksheet} | find_row')
    return -1

def find_column(worksheet, search):
    """Uses search term to find a column coordinate.

    Args:
        worksheet (FileStorage): The active worksheet in the excel file we are parsing.
        search (string): Search term required to locate a column.

    Returns:
        Integer: Coordinate for searched column.
    """
    for my_col in range(1, worksheet.max_column + 1):
        text = worksheet.cell(row = 1, column = my_col).value

        if text is not None:
            if not isinstance(text, datetime.datetime):
                if isinstance(text, str):
                    if search.lower() in text.lstrip().lower():
                        app.logger.info(f'{search} located in {worksheet}.')
                        return my_col

            if isinstance(text, datetime.datetime):
                date_str = str(text.strftime("%b"))
                if search.lower() in date_str.lower():
                    app.logger.info(f'{date_str} located in {worksheet}')
                    return my_col

    app.logger.error(f'{search} not found in {worksheet} | find_column')
    return -1
