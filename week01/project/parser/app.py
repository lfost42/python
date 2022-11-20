"""
Application server routes. 
"""
from flask import Flask, render_template, redirect, request, send_from_directory
from werkzeug.exceptions import RequestEntityTooLarge
import logging, os
from models import Upload
from uploader import check_file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            file = request.files['file']
            check_file(file)
            return render_template('report.html')
        
        except Exception as e:
            app.logger.warning(f'POST error {e}')
            return render_template('index.html')
