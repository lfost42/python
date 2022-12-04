"""
An exercise in pydantic and validators
"""
from pydantic import BaseModel, validator
import datetime

class Student(BaseModel):
    student_name: str
    student_id: int
    date_of_birth: datetime.date
    #student must be between 18 and 50 years old
    address: str
    state: str
    zip_code: str
    
    @validator('state')
    def state_check(cls, value):
        """
        Validates state is 2 characters. 
        """
        if len(value) != 2:
            raise ValueError('The state code length must be 2 characters')
        return value
    
    @validator('date_of_birth')
    def age_check(cls, value):
        """
        Validates student is between 18 and 50 years old. 
        """
        age = datetime.date.today() - value
        if age < datetime.timedelta(days=6570) or age > datetime.timedelta(days=18250):
            raise ValueError('The student must be between 18 and 50 years old')
        return value
    
student1 = Student(
    student_name = 'John Smith',
    student_id = 1111,
    date_of_birth = '2009-12-15',
    address = '34 Main St',
    state = 'CA',
    zip_code = '09823'
)

print(student1.dict())
