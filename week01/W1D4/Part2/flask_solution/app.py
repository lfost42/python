"""
Application server routes. 
"""
from flask import Flask, render_template, request
from validate import StudentModel

app = Flask(__name__)
print(__name__)

@app.route('/')
def index():
    return render_template('index.html', company_name='Tesla')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'GET':
        return render_template('add_student.html')
    else:
        print(request.form)

        try:
            student_data = StudentModel(**request.form)
            print(student_data.__dict__)
            return render_template('show_student.html', student = student_data)
        except Exception as e:
            print('Something went wrong')
            return render_template('show_student.html', student = e)
        




