from uploader import error_file, find_row, read_file, capture_data, find_file
from recordparser import voc_data, summary_data
import datetime

def month_year(file):
    """_summary_

    Args:
        file (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        date = file.split('expedia_report_monthly_',1)[1].split('_')
        year = date[1].split('.')[0]
        month = date[0].capitalize()
        try:
            int(year)
            if(not year or len(year) != 4 or int(year) < 0):
                #print('date inputed incorrectly')
                return -1
            else:
                num_month = month_to_num(month)
                if num_month == -1:
                    return -1
                else:
                    return[year, num_month, month]

        except OSError:
            print('Could not extract file year')

    except:
        error_file(file)
        #print('Error in file date')


def month_to_num(month):
    """_summary_

    Args:
        month (_type_): _description_

    Returns:
        _type_: _description_
    """
    if(month == 'January'):
        month_num = 1
    elif(month == 'Febuary'):
        month_num = 2
    elif(month == 'March'):
        month_num = 3
    elif(month == 'April'):
        month_num = 4
    elif(month == 'May'):
        month_num = 5
    elif(month == 'June'):
        month_num = 6
    elif(month == 'July'):
        month_num = 7
    elif(month == 'August'):
        month_num = 8
    elif(month == 'September'):
        month_num = 9
    elif(month == 'October'):
        month_num = 10
    elif(month == 'November'):
        month_num = 11
    elif(month == 'December'):
        month_num = 12
    else:
        #print('Month error in file name')
        return -1
    return month_num

def get_date(file, date):
    """_summary_

    Args:
        file (_type_): _description_
        date (_type_): _description_

    Returns:
        _type_: _description_
    """
    if(date == -1):
        print("Error: date not found")
        error_file(file)
    else:
        print("Success: date found")
        workbook = read_file(file)
        data_date = datetime.datetime(int(date[0]), date[1], 1)
        worksheet = workbook.active
        my_row = find_row(worksheet, data_date)

        if my_row:
            data = capture_data(worksheet, my_row)

        if not my_row or data == -1:
            print("Fields not found: file moved to error folder")
            error_file(file)
            return -1
        
        else:
            data_month = '' + date[2]
            print(f"Data for {date}: \n{data}")
            return data
        
def files_parsed():
    files = find_file()
    file_list = open('./parser/file_list.txt', "x")
    if files:
        for file in files:
            date = month_year(file)
            if date and date != -1:
                data = summary_data(file, date)
                if data != -1:
                    file_list.write(
                        "Summary Rolling MoM: {}\n".format(file))
                    voc_data(
                        file, 'VOC Rolling MoM', date)
                    file_list.write(
                        "VOC Rolling MoM: {}\n".format(file))