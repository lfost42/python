from validate import StudentModel
import datetime
from pydantic import ValidationError
import pytest


def test_validate_student_nominal():
    """
    GIVEN a helper class to validate Student data
    WHEN valid data is passed
    THEN check that the validation is successful.
    """
    student = StudentModel(
        student_name = 'John Smith',
        student_id = '1111',
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

def test_validate_student_invalid_student_id():
    """
    GIVEN a helper class to validate Student data
    WHEN invalid student_id is passed
    THEN check that the validation raises a ValueError.
    """
    with pytest.raises(ValueError):
        student = StudentModel(
            student_name = 'John Smith',
            student_id = 'asdf',
            date_of_birth = '1996-12-15',
            address = '34 Main St',
            state = 'CA',
            zip_code = '09823'
        )

def test_validate_student_invalid_state():
    """
    GIVEN a helper class to validate Student data
    WHEN invalid state code is passed
    THEN check that the validation raises a ValueError.
    """
    with pytest.raises(ValueError):
        student = StudentModel(
            student_name = 'John Smith',
            student_id = '1111',
            date_of_birth = '1996-12-15',
            address = '34 Main St',
            state = 'CAA',
            zip_code = '09823'
        )
