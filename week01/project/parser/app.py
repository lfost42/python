"""
Application server routes. 
"""
from flask import Flask, render_template
import logging, os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            #upload files
        except Exception as e:
            return render_template(index.html)
