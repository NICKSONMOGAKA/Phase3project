from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

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

def main():
    db = Database()

    while True:
        print("1. Create book")
        print("2. Create author")
        print("3. Create genre")
        print("4. Add author to book")
        print("5. Add genre to book")
        print("6. View all books")
        print("7. View all authors")
        print("8. View all genres")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            book = Book(title=title)
            db.create_book(book)
            print("Book created successfully!")
        elif choice == "2":
            name = input("Enter author name: ")
            author = Author(name=name)
            db.create_author(author)
            print("Author created successfully!")
        elif choice == "3":
            name = input("Enter genre name: ")
            genre = Genre(name=name)
            db.create_genre(genre)
            print("Genre created successfully!")
        elif choice == "4":
            book_id = int(input("Enter book ID: "))
            author_id = int(input("Enter author ID: "))
            book = db.db.query(Book).get(book_id)
            author = db.db.query(Author).get(author_id)
            db.add_author_to_book(book, author)
            print("Author added to book successfully!")
        elif choice == "5":
            book_id = int(input("Enter book ID: "))
            genre_id = int(input("Enter genre ID: "))
            book = db.db.query(Book).get(book_id)
            genre = db.db.query(Genre).get(genre_id)
            db.add_genre_to_book(book, genre)
            print("Genre added to book successfully!")
        elif choice == "6":
            books = db.db.query(Book).all()
            for book in books:
                print(f"Book {book.id}: {book.title}")
            print("Total books:", len(books))
        elif choice == "7":
            authors = db.db.query(Author).all()
            for author in authors:
                print(f"Author {author.id}: {author.name}")
            print("Total authors:", len(authors))
        elif choice == "8":
            genres = db.db.query(Genre).all()
            for genre in genres:
                print(f"Genre {genre.id}: {genre.name}")
            print("Total genres:", len(genres))
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()