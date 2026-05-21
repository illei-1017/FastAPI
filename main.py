from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# 오류 처리 관련 조건
class Course(BaseModel):
    course_name: str
    year: str
    semester: str
    grade: str

# GET
@app.get("/courses")
def get_courses():
    with open("courses.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

# POST
@app.post("/courses")
def add_course(course: Course):
    with open("courses.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    data.append(course.model_dump())
    
    with open("courses.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    return {"message": "추가 완료."}