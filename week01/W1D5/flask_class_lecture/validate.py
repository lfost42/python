from pydantic import BaseModel, validator
import datetime
from us.states import STATES_AND_TERRITORIES as all_states


class StudentModel(BaseModel):
    student_name: str
    student_id: int
    date_of_birth: datetime.date
    address: str
    state: str
    zip_code: str

    @validator('state')
    def state_check(cls, value):
        two_letter_abbr = [e.abbr for e in all_states]
        if value.upper() not in two_letter_abbr:
            raise ValueError('State Code is not valid')
        return value.upper()

        return value

    @validator('student_name')
    def student_name_capitalize(cls, value):
        return value.title()