from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    email = Column(String(80), nullable = False)
    password = Column(String(80), nullable = False)


class Pdf(Base):
    __tablename__ = "pdf"
    id = Column(Integer, primary_key = True)
    name = Column(String(255), nullable = False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)


engine = create_engine('mysql+mysqlconnector://root@localhost/web_scraping')
Base.metadata.create_all(engine)