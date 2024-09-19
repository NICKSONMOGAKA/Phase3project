from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship('Book', secondary='book_authors')

    def create(self, session):
        session.add(self)
        session.commit()

    def update(self, session, name):
        self.name = name
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()

    def read(self, session):
        return session.query(Author).filter_by(id=self.id).first()