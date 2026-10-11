from fastapi import FastAPI

app = FastAPI()

students = []


@app.get("/")
def home():
    return {"message": "AI Student Management"}


@app.get("/students")
def get_students():
    return students


@app.post("/students")
def add_student(name: str, department: str):

    student = {
        "name": name,
        "department": department
    }

    students.append(student)

    return {
        "message": "Student Added",
        "student": student
    }
