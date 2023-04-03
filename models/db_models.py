from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
import datetime

from db.base import db_gino


class Admins(db_gino.Model):
    __tablename__ = "admins"
    id_telegram = Column(Integer, primary_key=True)

    def __str__(self):
        return f'{self.id_telegram}'


class Customer(db_gino.Model):
    __tablename__ = "customers"
    id_telegram = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class Product(db_gino.Model):
    __tablename__ = "products"
    id_product = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    category = Column(String(50))
    category_code = Column(String(50))
    sub_category = Column(String(50))
    sub_category_code = Column(String(50))
    price = Column(Integer)
    quantity = Column(Integer)
    promotion = Column(Integer)
    new_product = Column(Integer)
    photo = Column(String(250))

    def __str__(self):
        return f'{self.id_product}, {self.name}, ' \
               f'{self.category}, {self.sub_category}, ' \
               f'{self.price}, {self.quantity}, {self.photo}, ' \
               f'{self.promotion}, {self.new_product}'


class Cart(db_gino.Model):
    __tablename__ = "cart"
    customer_id = Column(Integer)
    product_id = Column(Integer)
    photo = Column(String(250))
    quantity = Column(Integer)
    status_pay = Column(Integer, default=0)
