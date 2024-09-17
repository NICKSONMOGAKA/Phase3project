from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    employees = relationship("Employee", back_populates="department")

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'))
    department = relationship("Department", back_populates="employees")

def add_department(session, name):
    department = Department(name=name)
    session.add(department)
    session.commit()
    return department

def update_department(session, department_id, name):
    department = session.query(Department).filter(Department.id == department_id).first()
    if department:
        department.name = name
        session.commit()
        return department
    return None

def delete_department(session, department_id):
    department = session.query(Department).filter(Department.id == department_id).first()
    if department:
        session.delete(department)
        session.commit()
        return True
    return False

def add_employee(session, name, department_id):
    employee = Employee(name=name, department_id=department_id)
    session.add(employee)
    session.commit()
    return employee

def update_employee(session, employee_id, name, department_id):
    employee = session.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        employee.name = name
        employee.department_id = department_id
        session.commit()
        return employee
    return None

def delete_employee(session, employee_id):
    employee = session.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        session.delete(employee)
        session.commit()
        return True
    return False

def get_departments(session):
    return session.query(Department).all()

def get_employees(session):
    return session.query(Employee).all()

def get_department_by_name(session, name):
    return session.query(Department).filter(Department.name == name).first()

def get_department_by_id(session, department_id):
    return session.query(Department).filter(Department.id == department_id).first()

def get_employee_by_name(session, name):
    return session.query(Employee).filter(Employee.name == name).first()

def get_employee_by_id(session, employee_id):
    return session.query(Employee).filter(Employee.id == employee_id).first()

def get_employees_by_department(session, department_id):
    department = session.query(Department).filter(Department.id == department_id).first()
    return department.employees if department else []
