
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base


class Admin(Base):
    __tablename__ = "administrators"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    date = Column(DateTime)
    employee = Column(Integer, ForeignKey("employee.id"))
    id_employee = relationship("Employee")


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(255))
    surname = Column(String(255))
    phone = Column(Integer)
    date = Column(DateTime)



