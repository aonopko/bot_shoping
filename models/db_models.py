from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.base import db_gino


class Customer(db_gino.Model):
    __tablename__ = "customers"
    id_telegram = Column(Integer, unique=True, primary_key=True)
    name = Column(String(255), nullable=True)
    phone = Column(Integer)
    email = Column(String(255))


class Product(db_gino.Model):
    __tablename__ = "products"
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(50))
    category = Column(String(50))
    sub_category = Column(String(50))
    price = Column(Integer)
    quantity = Column(Integer)
    photo = Column(String(250))


class Order(db_gino.Model):
    __tablename__ = "orders"
    order_id = Column(Integer, unique=True, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id_telegram"))
    order_date = Column(DateTime)


class OrderProducts(db_gino.Model):
    __tablename__ = "order_products"
    order_id = Column(Integer, ForeignKey("orders.id"), ondelete="CASCADE")
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))
    quantity = Column(Integer)
