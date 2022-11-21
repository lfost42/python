"""
Application server routes.
"""
from flask import render_template, request
from records import summary_data, voc_data
from upload import error_file, archive_file, get_date, check_file
from handler import app

class My422Error(Exception):
    """An extension of the exception calss.

    Args:
        Exception (class)
    """

@app.route('/', methods=['GET', 'POST'])
def index():
    """_summary_

    Returns:
        html: report.html if upload/parsing is
        successful and 422.html/404.html if not.
    """
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        try:
            file = request.files['file']
            check = check_file(file)

            #returns 422 status and page
            if check == -1:
                app.logger.error(f'{file.filename} is a duplicate, moving to error folder')
                err_msg = 'Rejected: this is a duplicate file!'
                raise My422Error

            date = get_date(file)

            if date == -1:
                app.logger.critical(f'Rejected: could not parse date from {file.filename}')
                err_msg = f'Rejected: could not parse date from {file.filename}'
                raise My422Error

            data1 = summary_data(file)
            data2 = voc_data(file)
            if data1 == -1 or data2 == -1:
                app.logger.error(f'{file.filename} was not processed, \
                                 invalid or missing worksheets/data.')
                err_msg = 'Rejected: Bad data, please check worksheets/data.'
                raise My422Error

            # returns 200 status and report if all checks pass,
            # adds to processed.lst, and archives file
            app.logger.info(data1)
            app.logger.info(data2)

            with open('files/processed.lst', 'a', encoding = 'UTF-8') as file_list:
                file_list.write(f'{file.filename}\n')

            archive_file(file)
            app.logger.info(f'{file.filename} archived.')
            return render_template('report.html',
                                   file_name = file.filename,
                                   data1=data1,
                                   data2=data2), 200

        # returns 422 status/page
        except My422Error:
            error_file(file)
            return render_template('error/422.html',
                                       file_name = file.filename, message = err_msg), 422

    return render_template('error/405.html'), 405
