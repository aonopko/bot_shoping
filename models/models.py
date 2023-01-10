
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey, sql
from sqlalchemy.orm import relationship
from db.core import db_gino


class Admin(db_gino.Model):
    __tablename__ = "administrators"
    query: sql.Select

    id = Column(Integer, primary_key=True, index=True, unique=True)
    date = Column(DateTime)
    employee = Column(Integer, ForeignKey("employee.id"))
    id_employee = relationship("Employee")


class Employee(db_gino.Model):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(255))
    surname = Column(String(255))
    phone = Column(Integer)
    date = Column(DateTime)



