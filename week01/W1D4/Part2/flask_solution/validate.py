"""
Validates data passed into add_student form. 
"""
from pydantic import BaseModel, validator
import datetime
from us.states import STATES_AND_TERRITORIES as all_states
import zipcodes

class StudentModel(BaseModel):
    student_name: str
    student_id: int
    date_of_birth: datetime.date
    # student age between 18 and 50 all inclusive
    address: str
    state: str
    zip_code: str

    @validator('state')
    def state_check(cls, value):
        """
        Validates state code abbreviations. 
        """
        two_letter_abbr = [e.abbr for e in all_states]
        if value.upper() not in two_letter_abbr:
            raise ValueError('State Code is not valid')
        return value.upper()

    @validator('student_name')
    def student_name_capitalize(cls, value):
        """
        Capitalizes student name. 
        """
        return value.title()
    
    @validator('zip_code')
    def student_zip_code(cls, value):
        """
        Validates zip code. 
        """
        if zipcodes.is_real(value):
            return value
        else:
            raise ValueError('Invalid Zip Code')