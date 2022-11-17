from pydantic import BaseModel, validator
from datetime import date

class Student(BaseModel):
    student_name: str
    student_id: int
    date_of_birth: date
    #student must be between 18 and 50 years old
    address: str
    state: str
    zip_code: str
    
    @validator('state')
    def state_check(cls, value):
        if len(value) != 2:
            raise ValueError('The state code length must be 2 characters')
    
    @validator('date_of_birth')
    def age_check(cls, value):
        if value.year > 2004 or value.year < 1972:
            raise ValueError('The student must be between 18 and 50 years old')
    
student1 = Student(
    student_name = 'John Smith',
    student_id = 1111,
    date_of_birth = '1996-12-15',
    address = '34 Main St',
    state = 'CA',
    zip_code = '09823'
)

print(student1.dict())