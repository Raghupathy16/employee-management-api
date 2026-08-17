from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Employee(BaseModel):
    name:str
    dept:str


employees=[
    {"id":1, "name":"Raghu","Dept":"IT"},
    {"id":2,"name":"Vel","dept":"finance"},
    {"id":3,"name":"sam","dept":"Sales"}
]

@app.get("/")
def home():
    return{"message": "Employee Maangement"}
@app.get("/employees")

def get_employees():
    return(employees)

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"]==employee_id:
            return employee
    return {"messge":"employee not found"}

@app.post("/employees")

def create_employee(employee:Employee):

    new_employee={
        "id":len(employees)+1,
        "name": employee.name,
        "dept": employee.dept
    }

    employees.append(new_employee)
    return new_employee

@app.put("/employees/{employee_id}")
def update_employee(employee_id:int,employee:Employee):
    for existing_employee in employees:
        if existing_employee["id"]==employee_id:
            existing_employee["name"]=employee.name
            existing_employee["dept"]=employee.dept
            return existing_employee
    return{"message":"employee not found"}

@app.delete("/employees/{employee_id}")

def delete_employee(employee_id:int):
    for emp in employees:
        if emp["id"]==employee_id:
            employees.remove(emp)
            return{"message":"employee sucessfully deleted"}
    return{"employee not found"}