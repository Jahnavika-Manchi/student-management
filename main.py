from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
app = FastAPI()
students = []
next_id = 1
class Student(BaseModel):
    id: int
    name: str
    email: EmailStr
    course: str
    age: int
class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    course: str
    age: int
@app.get("/")
def home():
    return {"message": "Student API is running"}
@app.post("/students", status_code=201)
def create_student(student: StudentCreate):
    global next_id
    for existing_student in students:
        if existing_student.email == student.email:
            raise HTTPException(
                status_code=400,
                detail="User already exists"
            )
    new_student = Student(
        id=next_id,
        name=student.name,
        email=student.email,
        course=student.course,
        age=student.age
    )
    students.append(new_student)
    next_id += 1
    return new_student
@app.get("/students")
def get_students():
    return students
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
@app.put("/students/{student_id}")
def update_student(student_id: int, student_data: StudentCreate):
    for index, student in enumerate(students):
        if student.id == student_id:
            updated_student = Student(
                id=student_id,
                name=student_data.name,
                email=student_data.email,
                course=student_data.course,
                age=student_data.age
            )
            students[index] = updated_student
            return updated_student
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            students.pop(index)
            return {
                "message": "Student deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
@app.get("/search/", response_model=List[Student])
def search_students(course: Optional[str] = None):
    if course:
        return [student for student in students if student.course.lower() == course.lower()]
    return students