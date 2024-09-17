import subprocess

def run_cli_command(*args):
    result = subprocess.run(
        ['python', 'cli.py'] + list(args),
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip()

def test_list_books():
    output = run_cli_command("list-books")
    assert "No books found." in output

def test_create_book():
    # Ensure the database is initialized before running this test
    run_cli_command("create-author", "--name", "Sample Author")
    output = run_cli_command("create-book", "--title", "Sample Book", "--author-id", "1")
    assert "Created Book: ID=" in output

def test_list_authors():
    output = run_cli_command("list-authors")
    assert "No authors found." in output

def test_create_author():
    output = run_cli_command("create-author", "--name", "Sample Author")
    assert "Created Author: ID=" in output
