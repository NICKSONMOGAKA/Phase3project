import argparse
import sys
from database import get_books, add_book, get_authors, add_author

def list_books():
    books = get_books()
    if not books:
        print("No books found.")
    else:
        print("List of books:")
        for book in books:
            print(book)

def create_book(title, author_id):
    book = add_book(title, author_id)
    if book:
        print(f"Created Book: ID={book.id}")
    else:
        print("Failed to create book.")

def list_authors():
    authors = get_authors()
    if not authors:
        print("No authors found.")
    else:
        print("List of authors:")
        for author in authors:
            print(author)

def create_author(name):
    author = add_author(name)
    if author:
        print(f"Created Author: ID={author.id}")
    else:
        print("Failed to create author.")

def main():
    parser = argparse.ArgumentParser(description="CLI for managing books and authors.")
    subparsers = parser.add_subparsers(dest="command")

    # List Books
    subparsers.add_parser("list-books", help="List all books")

    # Create Book
    create_book_parser = subparsers.add_parser("create-book", help="Create a new book")
    create_book_parser.add_argument("--title", required=True, help="Title of the book")
    create_book_parser.add_argument("--author-id", type=int, required=True, help="ID of the author")

    # List Authors
    subparsers.add_parser("list-authors", help="List all authors")

    # Create Author
    create_author_parser = subparsers.add_parser("create-author", help="Create a new author")
    create_author_parser.add_argument("--name", required=True, help="Name of the author")

    args = parser.parse_args()

    if args.command == "list-books":
        list_books()
    elif args.command == "create-book":
        create_book(args.title, args.author_id)
    elif args.command == "list-authors":
        list_authors()
    elif args.command == "create-author":
        create_author(args.name)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
