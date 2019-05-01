from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql://root@localhost/seiya?charset=utf8')
Base = declarative_base(engine)

class Tenement(Base):
    __tablename__ = 'tenement'
    id = Column(Integer, primary_key=True)
    title = Column(String(40))
    unit = Column(String(16))
    area = Column(Integer)
    rent = Column(Integer)
    region = Column(String(10))


if __name__ == '__main__':
    Base.metadata.create_all()

