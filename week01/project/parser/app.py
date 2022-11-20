"""
Application server routes. 
"""
from flask import Flask, render_template, request
import logging
from models import Upload
from recordparser import list_files, summary_data, voc_data
from uploader import check_file, error_file
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

file_handler = RotatingFileHandler('files/expedia-info.log',
                                    maxBytes=16384,
                                    backupCount=20)
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in function %(funcName)s filename:%(filename)s:%(lineno)d]')
file_handler.setFormatter(file_formatter)
app.logger.addHandler(file_handler)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            file_list = open('files/file_list.txt', "a")
            file = request.files['file']
            check_file(file)
            list_files(file)
            data1 = summary_data(file)
            data2 = voc_data(file)
            app.logger.info(data1)
            app.logger.info(data2)
            return render_template('report.html', file_name = file.filename, data1=data1, data2=data2)
        
        except Exception as e:
            app.logger.warning(f'POST error {e}')
            error_file(file)
            return render_template('failure.html')

@app.route('/error', methods=['GET', 'POST'])
def error():
    if request.method == 'GET':
        return render_template('error.html')
    else:
        try:
            file_list = open('files/file_list.txt', "a")
            file = request.files['file']
            check_file(file)
            list_files(file)
            data1 = summary_data(file)
            app.logger.info(data1)
            data2 = voc_data(file)
            app.logger.info(data2)
            return render_template('report.html', file_name = file.filename, data1=data1, data2=data2)
        
        except Exception as e:
            app.logger.warning(f'POST error {e}')
            error_file(file)
            return render_template('failure.html')