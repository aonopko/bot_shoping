from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy import sql
from db.base import db_gino


class Admins(db_gino.Model):
    __tablename__ = "admins"
    id_telegram = Column(Integer, primary_key=True)
    name = Column(String(55))
    query: sql.Select

    __str__



class Customer(db_gino.Model):
    __tablename__ = "customers"
    id_telegram = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    phone = Column(Integer, unique=True)
    email = Column(String(255), unique=True)


class Product(db_gino.Model):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    category = Column(String(50))
    sub_category = Column(String(50))
    price = Column(Integer)
    quantity = Column(Integer)
    photo = Column(String(250))

    query: sql.Select

class Order(db_gino.Model):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id_telegram"))
    order_date = Column(DateTime)


class OrderProduct(db_gino.Model):
    __tablename__ = "order_products"
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
