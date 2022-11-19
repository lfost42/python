import os
import datetime
import shutil
import openpyxl

def find_file():
    """_summary_

    Returns:
        _type_: _description_
    """
    try:
        path_array = []
        for file in os.listdir('./parser/external_files'):
            if file.startswith('expedia_report_monthly_'):
                path = './parser/external_files/{file}'
                path_array.append(path)
                src_folder = '/parser/external_files/'
                if os.path.exists(src_folder):
                    shutil.move(path, src_folder)
            else:
                file_path = f'./parser/external_files/{file}'
                error_file(file_path)

        if len(path_array) > 0:
            return path_array
    except:
        #print('Unable to load file')

def read_file(file):
    """_summary_

    Args:
        file (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        if not file:
            print('No file found under naming convention: expedia_report_monthly_MONTH_YEAR.xlsx')
        else:
            try:
                workbook = openpyxl.load_workbook(file)
                return workbook
            except:
                print('Data was not able to load')

    except:
        print('Error while reading File')

def archive_file(file):
    """_summary_

    Args:
        arch_file (_type_): _description_
    """
    src_folder = "./parser/files/archived/"
    if os.path.exists(src_folder):
        shutil.move(file, src_folder)

def error_file(file):
    """_summary_

    Args:
        error_file (_type_): _description_
    """
    file_name = file.split('./parser/files/archived/')[1]
    src_folder = "./parser/files/archived/"
    print(f"File moved to {file_name}")

    if len(os.listdir('./parser/error')) > 0:
        for file in os.listdir('./parser/files/error'):
            if file == file.split('./parser/files/external_files/')[1]:
                break
            else:
                if os.path.exists(src_folder):
                    shutil.move(file, src_folder)

    else:
        if os.path.exists(src_folder):
            shutil.move(file, src_folder)
            
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
    #print('Row with matching date not found')

def find_column(worksheet, name):
    """_summary_

    Args:
        worksheet (_type_): _description_
        name (_type_): _description_

    Returns:
        _type_: _description_
    """
    for i_col in range(1, worksheet.max_column + 1):
        for i_row in range(1, worksheet.max_row + 1):
            if worksheet.cell(row = i_row, column = i_col).value == name:
                return i_col
    #print('Column with matching date not found')