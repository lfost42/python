from app import Student
import datetime

def test_validate_student_nominal():
    student = Student(
    student_name = 'John Smith',
    student_id = 1111,
    date_of_birth = '1996-12-15',
    address = '34 Main St',
    state = 'CA',
    zip_code = '09823'
)
    
    assert student.student_name == 'John Smith'
    assert student.student_id == 1111
    assert student.date_of_birth == datetime.date(1996, 12, 15)
    assert student.address == '34 Main St'
    assert student.state == 'CA'
    assert student.zip_code == '09823'
    
