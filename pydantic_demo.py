# ye lagare hain ki ye always string hoga name ya ni

from typing import Optional

from pydantic import BaseModel, Field
class Student(BaseModel):
    name: str = 'praku' 
    age: Optional[int] = None

    #  = praku is default value
    cgpa: float = Field(gt = 0, lt = 10)
    


new_student = {'name': '', 'cgpa': 8.5}
student = Student(**new_student)
print(student)