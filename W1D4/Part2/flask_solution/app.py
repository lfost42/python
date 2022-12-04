"""
Application server routes. 
"""
from flask import Flask, render_template, request  # brings the Flask class from the flask module into scope so we can use it
from validate import StudentModel

# Creates a new flask object and assign it to a variable app; __name__ lets us run the app directly or import it as a module.
app = Flask(__name__)
print(__name__)


# Alters the functionality of our code, associating following fuctions with the route. '/' refers to the home page.
@app.route('/')
def index():
    return render_template('index.html', company_name='Tesla')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    """
    Adds student from request form or shows student data. 
    """
    if request.method == 'GET':
        return render_template('add_student.html')
    else:
        print(request.form)

        try:
            student_data = StudentModel(**request.form)
            print(student_data.__dict__)
            return render_template('show_student.html', student=student_data)
        # log this
        except Exception as e:
            print('Something went wrong')
            return render_template('show_student.html', student=e)
