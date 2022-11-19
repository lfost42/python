from uploader import find_column, read_file, find_row, error_file, archive_file
import datetime
                
def summary_data(worksheet, my_row):
    calls = worksheet.cell(row = my_row, column = find_column(worksheet, 'Calls Offered')).value
    #TODO: strip leading spaces
    abandon = worksheet.cell(row = my_row, column = find_column(worksheet, ' Abandon after 30s')).value
    fcr = worksheet.cell(row = my_row, column = find_column(worksheet, 'FCR')).value
    dsat = worksheet.cell(row = my_row, column = find_column(worksheet, 'DSAT ')).value
    csat = worksheet.cell(row = my_row, column = find_column(worksheet, 'CSAT ')).value

    if calls and abandon and fcr and dsat and csat:
        data = {
        'Calls Offered': calls,
        'Abandon after 30s': "{:.2%}".format(abandon),
        'FCR': "{:.2%}".format(fcr),
        'DSAT': "{:.2%}".format(dsat),
        'CSAT': "{:.2%}".format(csat)
        }
        return data
    else:
        return -1

def voc_data(file, sheet, date):
    if(date == -1):
        print("Error: could not extract date")
        error_file(file)
    else:
        print("Success: date extracted")
        data_date = datetime.datetime(int(date[0]), date[1], 1)
        workbook = read_file(file)
        worksheet2 = workbook[sheet]
        my_col = find_column(worksheet2, data_date)

        if not my_col:
            my_col = find_column(worksheet2, date[2])
    
        if not my_col:
            error_file(file)
            #print("Column not found, file moved to Error folder")
            
        # Check Promoters
        my_row = find_row(worksheet2, 'Promoters')
        promoters = check_score('Promoters', worksheet2.cell(row = my_row, column = my_col).value)

        # Check Passives
        my_row = find_row(worksheet2, 'Passives')
        passives = check_score('Passives', worksheet2.cell(row = my_row, column = my_col).value)
        
        # Check Decractors
        my_row = find_row(worksheet2, 'Dectractors')
        dectractors = check_score('Dectractors', worksheet2.cell(row = my_row, column = my_col).value)

        if promoters and passives and dectractors:
            #print("Promoters: {promoters} \n\tPassives: {passives} \n\tDectractors: {dectractors}")
            archive_file(file)
        
        else:
            #print("Fields not found, file moved to error_files folder")
            error_file(file)

def check_score(category, value):
    if category == 'Promoters':
        if value > 200:
            return 'good'
        else:
            return 'bad'
    elif category == 'Passives':
        if value > 100:
            return 'good'
        else:
            return 'bad'
    elif category == 'Dectractors':
        if value > 100:
            return 'good'
        else:
            return 'bad'
    else:
        print(f"Value for {category} is missing or invalid.")
