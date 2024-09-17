import subprocess

def run_cli_command(*args):
    result = subprocess.run(["python", "book_manager/cli.py"] + list(args), capture_output=True, text=True)
    return result.stdout

def test_list_departments():
    output = run_cli_command("list-departments")
    assert "No departments found." in output

def test_create_department():
    output = run_cli_command("create-department", "--department-name", "IT")
    assert "Created Department: ID=" in output

def test_list_employees():
    output = run_cli_command("list-employees")
    assert "No employees found." in output
