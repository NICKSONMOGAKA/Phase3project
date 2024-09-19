from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship('Book', secondary='book_genres')

    def create(self, session):
        session.add(self)
        session.commit()

    def read(self, ):
        return self  

    def update(self, session, name):
        self.name = name
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()