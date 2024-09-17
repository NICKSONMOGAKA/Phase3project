
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from book_manager.models import Author, Book, Base

DATABASE_URL = "sqlite:///books.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database initialized.")

def create_book(title, author_id):
    db = SessionLocal()
    author = db.query(Author).filter(Author.id == author_id).first()
    if author:
        book = Book(title=title, author=author)
        db.add(book)
        db.commit()
        print(f"Book '{title}' created.")
    else:
        print("Author not found.")
    db.close()

def list_books():
    db = SessionLocal()
    books = db.query(Book).all()
    for book in books:
        print(f"Title: {book.title}, Author: {book.author.name}")
    db.close()

def create_author(name):
    db = SessionLocal()
    author = Author(name=name)
    db.add(author)
    db.commit()
    print(f"Author '{name}' created.")
    db.close()

def list_authors():
    db = SessionLocal()
    authors = db.query(Author).all()
    for author in authors:
        print(f"Author: {author.name}")
    db.close()
