from app import Student
from datetime import date

def test_new_student():
    new_student = Student(
        student_name = 'John Smith',
        student_id = 1111,
        date_of_birth = date(year=2004, month=9, day=13),
        address = '23 Side Street',
        state = 'PA',
        zip_code = '16802'
    )

    assert new_student.student_name == 'John Smith'
    assert new_student.student_id == 1111
    assert new_student.date_of_birth == date(year=2004, month=9, day=13)
    assert new_student.address == '23 Side Street'
    assert new_student.state == 'PA'
    assert new_student.zip_code == '16802'
