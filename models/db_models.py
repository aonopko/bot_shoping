from sqlalchemy import Integer, String, Column, DateTime, ForeignKey, DATETIME
from datetime import datetime

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
    customer_id = Column(Integer, ForeignKey("customers.id_telegram"))
    product_id = Column(Integer, ForeignKey("products.id_product"))
    quantity = Column(Integer)
    status_pay = Column(Integer, default=0)
    price = Column(Integer)
    photo = Column(String(250))
    created_at = Column(DateTime())

    # def __init__(self, data):
    #     self.data = data
    #     self.index = 0
    #
    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     if self.index >= len(self.data):
    #         raise StopIteration
    #     value = self.data[self.index]
    #     self.index += 1
    #     return value
