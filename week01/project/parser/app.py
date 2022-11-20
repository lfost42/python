"""
Application server routes. 
"""
from flask import render_template, request, status
from records import check_file, summary_data, voc_data
from upload import error_file, archive_file, get_date
from handler import app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            file = request.files['file']
            
            check = check_file(file)
            date = get_date(file)
            data1 = summary_data(file)
            data2 = voc_data(file)

            
            # returns 422 status and page
            if check == -1:
                app.logger.error(f'{file.filename} is a duplicate, moving to error folder')
                message = 'Rejected: this is a duplicate file!'
            if date == -1:
                app.logger.error(f'Rejected: could not parse date from {file.filename}')
                mesage = f'Rejected: could not parse date from {file.filename}'
            if data1 == -1 or data2 == -1:
                app.logger.error(f'{file.filename} was not processed, invalid or missing worksheets/data.')
                message = 'Rejected: Bad data, please check worksheets/data.'
            
            if check == -1 or date == -1 or data1 == -1 or data2 == -1:    
                error_file(file)
                return render_template('422.html', file_name = file.filename, message=message), status.HTTP_422_CREATED
            
            #returns 201 status and report
            app.logger.makeRecord(data1)
            app.logger.makeRecord(data2)
            
            #TODO: move to handler
            file_list = open('files/processed.lst', "a")
            file_list.write(f'{file.filename}')
            
            archive_file(file)
            return render_template('report.html', file_name = file.filename, data1=data1, data2=data2), status.HTTP_201_CREATED
        
        #returns 404 status/page
        except Exception as e:
            app.logger.exception(f'POST error, file not processed: {e}')
            return render_template('404.html'), status.HTTP_404_CREATED
