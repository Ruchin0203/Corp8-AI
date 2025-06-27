from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Student(BaseModel):

    name: str = "Ruchin"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')

new_student = {"name":"Ruchin", "age":"23", "email":"abc@gmail.com"} # <-type coercing(jate j sring mathi int kari de)

student = Student(**new_student)

print(student)

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()