from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    authors = relationship('Author', secondary='book_authors')
    genres = relationship('Genre', secondary='book_genres')

    def __init__(self, title):
        self.title = title

    def create(self, session):
        session.add(self)
        session.commit()

    def read(self):
        return self  

    def update(self, session, title):
        self.title = title
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()