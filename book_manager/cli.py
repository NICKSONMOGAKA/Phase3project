import argparse
from book_manager.utils import list_departments, find_department_by_name, find_department_by_id, create_department, update_department, delete_department, list_employees, find_employee_by_name, find_employee_by_id, create_employee, update_employee, delete_employee, list_employees_in_department
from book_manager.database import init_db

def main():
    parser = argparse.ArgumentParser(description="Department and Employee Management System")
    parser.add_argument("command", choices=[
        "list-departments", "find-department-by-name", "find-department-by-id",
        "create-department", "update-department", "delete-department",
        "list-employees", "find-employee-by-name", "find-employee-by-id",
        "create-employee", "update-employee", "delete-employee",
        "list-employees-in-department"], help="Command to execute")
    parser.add_argument("--name", help="Department or employee name")
    parser.add_argument("--department-id", type=int, help="ID of the department")
    parser.add_argument("--employee-id", type=int, help="ID of the employee")
    parser.add_argument("--department-name", help="Name of the department for creating")
    parser.add_argument("--employee-name", help="Name of the employee for creating or updating")
    parser.add_argument("--new-department-name", help="New department name for updating")
    parser.add_argument("--new-employee-name", help="New employee name for updating")

    args = parser.parse_args()

    init_db()

    if args.command == "list-departments":
        list_departments()
    elif args.command == "find-department-by-name":
        if args.name:
            find_department_by_name(args.name)
        else:
            print("Please provide --name to find a department by name.")
    elif args.command == "find-department-by-id":
        if args.department_id:
            find_department_by_id(args.department_id)
        else:
            print("Please provide --department-id to find a department by ID.")
    elif args.command == "create-department":
        if args.department_name:
            create_department(args.department_name)
        else:
            print("Please provide --department-name to create a department.")
    elif args.command == "update-department":
        if args.department_id and args.new_department_name:
            update_department(args.department_id, args.new_department_name)
        else:
            print("Please provide --department-id and --new-department-name to update a department.")
    elif args.command == "delete-department":
        if args.department_id:
            delete_department(args.department_id)
        else:
            print("Please provide --department-id to delete a department.")
    elif args.command == "list-employees":
        list_employees()
    elif args.command == "find-employee-by-name":
        if args.name:
            find_employee_by_name(args.name)
        else:
            print("Please provide --name to find an employee by name.")
    elif args.command == "find-employee-by-id":
        if args.employee_id:
            find_employee_by_id(args.employee_id)
        else:
            print("Please provide --employee-id to find an employee by ID.")
    elif args.command == "create-employee":
        if args.employee_name and args.department_id:
            create_employee(args.employee_name, args.department_id)
        else:
            print("Please provide --employee-name and --department-id to create an employee.")
    elif args.command == "update-employee":
        if args.employee_id and args.new_employee_name and args.department_id:
            update_employee(args.employee_id, args.new_employee_name, args.department_id)
        else:
            print("Please provide --employee-id, --new-employee-name, and --department-id to update an employee.")
    elif args.command == "delete-employee":
        if args.employee_id:
            delete_employee(args.employee_id)
        else:
            print("Please provide --employee-id to delete an employee.")
    elif args.command == "list-employees-in-department":
        if args.department_id:
            list_employees_in_department(args.department_id)
        else:
            print("Please provide --department-id to list employees in a department.")

if __name__ == "__main__":
    main()
