from sqlalchemy import Column, String, Integer, Text, DateTime
from db.connect import Base


class Admin(Base):
    __tablename__ = "administrators"
    id_admin = Column(Integer, primary_key=True, index=True, unique=True)
    id_employee = Column(Integer)
    date = Column(DateTime)
