from uploader import find_column, read_file, find_row, error_file, archive_file
from flask import Flask
import re

app = Flask(__name__)

def summary_data(file):
    workbook = read_file(file)
    worksheet = workbook['Summary Rolling MoM']
    
    if not worksheet:
        app.logger.error('Summary Rolling MoM: worksheet not found')
        error_file(file)
        
    date = get_date(file) 
    datef = f'{date[1]}-{date[0]}'
    
    my_row = find_row(worksheet, datef)
    if not my_row:
        app.logger.error(f'Cannot find date in Summary worksheet: {datef}')
        return -1
    
    calls = worksheet.cell(row = my_row, column = find_column(worksheet, 'Calls Offered')).internal_value
    abandon = worksheet.cell(row = my_row, column = find_column(worksheet, 'Abandon after 30s')).internal_value
    fcr = worksheet.cell(row = my_row, column = find_column(worksheet, 'FCR')).internal_value
    dsat = worksheet.cell(row = my_row, column = find_column(worksheet, 'DSAT ')).internal_value
    csat = worksheet.cell(row = my_row, column = find_column(worksheet, 'CSAT ')).internal_value

    if calls and abandon and fcr and dsat and csat:
        abandon = "{:.2%}".format(abandon)
        fcr = "{:.2%}".format(fcr)
        dsat = "{:.2%}".format(dsat)
        csat = "{:.2%}".format(csat)
        data = f"Calls Offered: {calls} | Abandon after 30s: {abandon} | FCR: {fcr} | DSAT: {dsat} | CSAT: {dsat}"
        
        return data
    else:
        return -1

def voc_data(file):
    workbook = read_file(file)
    worksheet = workbook['VOC Rolling MoM']
    
    if not worksheet:
        app.logger.error('VOC Rolling MoM worksheet not found')
        error_file(file)
    
    #TODO: remove redundancy in getting and setting
    date = get_date(file) 
    month = f'{date[1]}'
    
    my_col = find_column(worksheet, month)
    if not my_col:
        app.logger.error(f'Cannot find date in Summary worksheet: month:{month}')
        error_file(file)
        return -1
    
    # Check Promoters
    my_row = find_row(worksheet, 'Promoters')
    promoters = check_score('Promoters', worksheet.cell(row = my_row, column = my_col).internal_value)

    # Check Passives
    my_row = find_row(worksheet, 'Passives')
    passives = check_score('Passives', worksheet.cell(row = my_row, column = my_col).internal_value)
    
    # Check Decractors
    my_row = find_row(worksheet, 'Dectractors')
    dectractors = check_score('Dectractors', worksheet.cell(row = my_row, column = my_col).internal_value)

    if promoters and passives and dectractors:
        data = f'Promoters: {promoters} | Passives: {passives} | Dectractors: {dectractors}'
        archive_file(file)
        return data
    
    else:
        app.logger.error("ERROR: missing field, file moved to error folder, recordparser.py")
        error_file(file)
        return -1

def check_score(category, score):
    if category == 'Promoters':
        if score > 200:
            return 'good'
        else:
            return 'bad'
    elif category == 'Passives':
        if score > 100:
            return 'good'
        else:
            return 'bad'
    elif category == 'Dectractors':
        if score > 100:
            return 'good'
        else:
            return 'bad'
    else:
        print(f"Value for {category} is missing or invalid.")

def check_year(file):
    filename = file.filename
    digits = re.findall('[0-9]+', filename)
    
    if (not digits or len(digits[0]) != 4):
        error_file(file)
        exit()
        return -1
    else:
        return digits[0][-2:]

def check_month(file):
    filename = file.filename.lower()
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    
    for i in months:
        if i in filename:
            return i
    app.logger.error('ERROR: unable to extract month, recordparser.py')
    return -1

def get_date(file):
    year = check_year(file)
    month = check_month(file)
    return [year, month]

def list_files(file):
    file_list = open('files/file_list.txt', "a")
    sum_check = summary_data(file)
    voc_check = voc_data(file)
    
    if sum_check !=1 and voc_check != -1:
        file_list.write(
                f'Summary Rolling MoM: {file}\n')
