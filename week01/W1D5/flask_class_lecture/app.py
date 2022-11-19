from flask import Flask, render_template, request, url_for, redirect
from validate import StudentModel

import logging, os
from logging.handlers import RotatingFileHandler

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# --------------------------
file_handler = RotatingFileHandler('flask-student-info.log',
                                    maxBytes=16384,
                                    backupCount=20)
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in function %(funcName)s filename:%(filename)s:%(lineno)d]')
file_handler.setFormatter(file_formatter)
app.logger.addHandler(file_handler)
# ---------------------------
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'app.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String, nullable=False)
    student_id = db.Column(db.Integer, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    address = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    zip_code = db.Column(db.String, nullable=False)

    def __init__(self, student_name, student_id, date_of_birth, address, state, zip_code):
        self.student_name = student_name
        self.student_id = int(student_id)
        self.date_of_birth = date_of_birth
        self.address = address
        self.state = state
        self.zip_code = zip_code

    def __repr__(self):
        return f'{self.id}-{self.student_name}-{self.student_id}-{self.date_of_birth}'

# ----------------------------
app.logger.info('Starting the Flask Student App ...')
@app.route('/')
def index():
    app.logger.info('Accesing the index page')
    return render_template('index.html', company_name='SmoothStack')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'GET':
        return render_template('add_student.html')
    else:
        print(request.form)
        app.logger.info(f'Trying to post data to app...{request.form}')
        try:
            validated_student_data = StudentModel(**request.form)
            #print(student_data.__dict__)
            app.logger.info(f'Successful post data to app...{request.form}')
            print(student_data)
            new_student = Student(**dict(validated_student_data))
            db.session.add(new_student)
            db.session.commit()
            app.logger.info(f'Successful database insertion...{request.form}')

            return redirect(url_for('list_students'))
        except Exception as e:
            app.logger.error(f'Failed and threw an exception {e}')
            print('Something went wrong')
            return render_template('students.html', students = e)
        
        
@app.route('/students')
def list_students():
    students = Student.query.order_by(Student.id).all()
    return render_template('students.html', students=students)




