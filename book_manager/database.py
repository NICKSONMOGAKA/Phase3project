from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
DATABASE_URL = "sqlite:///books.db"

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author')

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
        db.refresh(book)
        db.close()
        return book
    else:
        db.close()
        return None

def list_books():
    db = SessionLocal()
    books = db.query(Book).all()
    db.close()
    return books

def create_author(name):
    db = SessionLocal()
    author = Author(name=name)
    db.add(author)
    db.commit()
    db.refresh(author)
    db.close()
    return author

def list_authors():
    db = SessionLocal()
    authors = db.query(Author).all()
    db.close()
    return authors
