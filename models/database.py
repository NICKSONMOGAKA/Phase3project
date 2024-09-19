from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    authors = []
    genres = []

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String)

DATABASE_URL = "sqlite:///books.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(engine)

class Database:
    def __init__(self):
        self.db = SessionLocal()

    def create_book(self, book):
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)

    def create_author(self, author):
        self.db.add(author)
        self.db.commit()
        self.db.refresh(author)

    def create_genre(self, genre):
        self.db.add(genre)
        self.db.commit()
        self.db.refresh(genre)

    def add_author_to_book(self, book, author):
        book.authors.append(author)
        self.db.commit()

    def add_genre_to_book(self, book, genre):
        book.genres.append(genre)
        self.db.commit()