from book_manager.database import SessionLocal
from book_manager.models import add_department, update_department, delete_department, add_employee, update_employee, delete_employee, get_departments, get_employees, get_department_by_name, get_department_by_id, get_employee_by_name, get_employee_by_id, get_employees_by_department

def list_departments():
    with SessionLocal() as session:
        departments = get_departments(session)
        if departments:
            for dept in departments:
                print(f"Department ID: {dept.id}, Name: {dept.name}")
        else:
            print("No departments found.")

def find_department_by_name(name):
    with SessionLocal() as session:
        dept = get_department_by_name(session, name)
        if dept:
            print(f"Department ID: {dept.id}, Name: {dept.name}")
        else:
            print("Department not found.")

def find_department_by_id(department_id):
    with SessionLocal() as session:
        dept = get_department_by_id(session, department_id)
        if dept:
            print(f"Department ID: {dept.id}, Name: {dept.name}")
        else:
            print("Department not found.")

def create_department(name):
    with SessionLocal() as session:
        dept = add_department(session, name)
        print(f"Created Department: ID={dept.id}, Name={dept.name}")

def update_department(department_id, name):
    with SessionLocal() as session:
        dept = update_department(session, department_id, name)
        if dept:
            print(f"Updated Department: ID={dept.id}, Name={dept.name}")
        else:
            print("Department not found.")

def delete_department(department_id):
    with SessionLocal() as session:
        if delete_department(session, department_id):
            print("Department deleted.")
        else:
            print("Department not found.")

def list_employees():
    with SessionLocal() as session:
        employees = get_employees(session)
        if employees:
            for emp in employees:
                print(f"Employee ID: {emp.id}, Name: {emp.name}, Department ID: {emp.department_id}")
        else:
            print("No employees found.")

def find_employee_by_name(name):
    with SessionLocal() as session:
        emp = get_employee_by_name(session, name)
        if emp:
            print(f"Employee ID: {emp.id}, Name: {emp.name}, Department ID: {emp.department_id}")
        else:
            print("Employee not found.")

def find_employee_by_id(employee_id):
    with SessionLocal() as session:
        emp = get_employee_by_id(session, employee_id)
        if emp:
            print(f"Employee ID: {emp.id}, Name: {emp.name}, Department ID: {emp.department_id}")
        else:
            print("Employee not found.")

def create_employee(name, department_id):
    with SessionLocal() as session:
        emp = add_employee(session, name, department_id)
        print(f"Created Employee: ID={emp.id}, Name={emp.name}, Department ID={emp.department_id}")

def update_employee(employee_id, name, department_id):
    with SessionLocal() as session:
        emp = update_employee(session, employee_id, name, department_id)
        if emp:
            print(f"Updated Employee: ID={emp.id}, Name={emp.name}, Department ID={emp.department_id}")
        else:
            print("Employee not found.")

def delete_employee(employee_id):
    with SessionLocal() as session:
        if delete_employee(session, employee_id):
            print("Employee deleted.")
        else:
            print("Employee not found.")

def list_employees_in_department(department_id):
    with SessionLocal() as session:
        employees = get_employees_by_department(session, department_id)
        if employees:
            print(f"Employees in Department ID {department_id}:")
            for emp in employees:
                print(f" - Employee ID: {emp.id}, Name: {emp.name}")
        else:
            print("No employees found in this department.")
