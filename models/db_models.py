from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.base import db_gino


class Customer(db_gino.Model):
    __tablename__ = "customer"
    id_telegram = Column(Integer, unique=True, primary_key=True)
    name = Column(String(255))
    phone = Column(Integer)
    email = Column(String(255))


class Product(db_gino.Model):
    __tablename__ = "product"
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(50))
    price = Column(Integer)
    quantity = Column(Integer)
    photo = Column(String(250))





