from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql://root@localhost/seiya?charset=utf8')
Base = declarative_base(engine)

class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    director = Column(String(16))
    grade = Column(Float)
    review_num = Column(Integer)
    country = Column(String(10))
    tags = Column(String(20))

if __name__ == '__main__':
    Base.metadata.create_all()

