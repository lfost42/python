'''
Parses data from records and processes them into appripriate summaries.
'''
from file_handler import read_file
from name_parser import get_date
from worksheet_search import find_column, find_row
from logging_handler import app

#To refactor as a class method once database is complete.
def summary_data(file):
    '''Finds Summary worksheet and parses records for Summary Report.

    Args:
        file (FileStorage): The file we want to parse.

    Returns:
        String: The data we need to provide the Summary Report.
        integer: -1 if the file or data could not be found.
    '''
    workbook = read_file(file)
    worksheet = workbook['Summary Rolling MoM']

    if not worksheet:
        app.logger.error(f'Could not locate Summary Rolling MoM in {file} | summary_data')
        return -1

    date = get_date(file)
    datef = f'{date[1]}-{date[0]}'

    my_row = find_row(worksheet, datef)
    if not my_row:
        app.logger.error(f'Cannot find {datef} in Summary Rolling MoM: {file} | summary_data')
        return -1

    calls = worksheet.cell(row = my_row, column = find_column
                           (worksheet, 'Calls Offered')).internal_value
    abandon = worksheet.cell(row = my_row, column = find_column
                             (worksheet, 'Abandon after 30s')).internal_value
    fcr = worksheet.cell(row = my_row, column = find_column
                         (worksheet, 'FCR')).internal_value
    dsat = worksheet.cell(row = my_row, column = find_column
                          (worksheet, 'DSAT ')).internal_value
    csat = worksheet.cell(row = my_row, column = find_column
                          (worksheet, 'CSAT ')).internal_value

    if calls and abandon and fcr and dsat and csat:
        abandon = f'{abandon:.2%}'
        fcr = f'{fcr:.2%}'
        dsat = f'{dsat:.2%}'
        csat = f'{csat:.2%}'
        app.logger.critical(csat)
        data = (f'Calls Offered: {calls} | \
        Abandon after 30s: {abandon} | FCR: {fcr} \
        | DSAT: {dsat} | CSAT: {dsat}')

        app.logger.info(f'Summary data parsed for {file}.')
        return data
    app.logger.error(f'Bad data: could not parse summary info for {file} | summary_data')
    return -1

#To refactor as a class method once database is complete.
def voc_data(file):
    '''Finds VOC worksheet and parses records for VOC Report.

    Args:
        file (FileStorage): The file we want to parse.

    Returns:
        String: The data we need to provide the VOC Report.
        integer: -1 if the file or data could not be found.
    '''
    workbook = read_file(file)
    worksheet = workbook['VOC Rolling MoM']

    if not worksheet:
        app.logger.error(f'VOC Rolling MoM worksheet not found in {file.filename} | voc_data')
        return -1

    date = get_date(file)
    month = f'{date[1]}'

    my_col = find_column(worksheet, month)
    if not my_col:
        app.logger.error(f'Cannot find {month} in Summary worksheet for file: {file} | voc_data')
        return -1

    # Check Promoters
    my_row = find_row(worksheet, 'Promoters')
    promoters = check_score('Promoters',
                            worksheet.cell(row = my_row, column = my_col).internal_value)

    # Check Passives
    my_row = find_row(worksheet, 'Passives')
    passives = check_score('Passives',
                           worksheet.cell(row = my_row, column = my_col).internal_value)

    # Check Decractors
    my_row = find_row(worksheet, 'Dectractors')
    dectractors = check_score('Dectractors',
                              worksheet.cell(row = my_row, column = my_col).internal_value)

    if promoters and passives and dectractors:
        data = f'Promoters: {promoters} | Passives: {passives} | Dectractors: {dectractors}'
        app.logger.info(f'VOC data processed from {file.filename}.')
        return data

    app.logger.error(f'ERROR: missing field, {file.filename} moved to error folder | voc_data')
    return -1

def check_score(category, score):
    '''_summary_

    Args:
        category (string): Group identifier.
        score (integer): Numeric value of identifier.

    Returns:
        string: Good or bad.
    '''
    result = 'good' if category == 'Promoters' and score >= 200 else 'bad'
    result = 'good' if category == 'Passives' and score >= 100 else 'bad'
    result = 'good' if category == 'Dectractors' and score >= 100 else 'bad'

    if result != 'good' or result != 'bad':
        app.logger.error(f'Value for {category} is missing or invalid | check_score')

    app.logger.info('Promoters, Passives, and Dectractors scores found.')
    return result
