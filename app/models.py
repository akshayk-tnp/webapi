from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    firstName = Column(String, nullable=False)
    lastName= Column(String,nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    # class Config:
    #        orm_mode=True
    

class ChartData(Base):
    __tablename__ = "chartdata"
    id = Column(Integer, primary_key=True, nullable=False)
    value= Column(Integer, nullable=False)
    labels= Column(String,nullable=False)


class ChartData1(Base):
    __tablename__ = "chartdata1"
    id = Column(Integer, primary_key=True, nullable=False)
    value= Column(Integer, nullable=False)
    labels= Column(String,nullable=False)

    # class Config:
    #        orm_mode=True

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, nullable=False)
    content= Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    topic=Column(String, nullable=False)
    # owner_id= Column(String, nullable=False)

    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")