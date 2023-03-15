from sqlalchemy import Integer, String, Column, DateTime, ForeignKey

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
    phone = Column(Integer, unique=True)
    email = Column(String(255), unique=True)


class Product(db_gino.Model):
    __tablename__ = "products"
    id_product = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    category = Column(String(50))
    category_code = Column(Integer)
    sub_category = Column(String(50))
    sub_category_code = Column(Integer)
    price = Column(Integer)
    quantity = Column(Integer)
    promotion = Column(Integer)
    new_product = Column(Integer)
    photo = Column(String(250))

    def __str__(self):
        return f'{self.id_product}, {self.name},' \
               f'{self.category}, {self.sub_category}' \
               f'{self.price}, {self.quantity}, {self.photo}'


class Order(db_gino.Model):
    __tablename__ = "orders"
    id_order = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id_telegram"))
    order_date = Column(DateTime)


class OrderProduct(db_gino.Model):
    __tablename__ = "order_products"
    order_id = Column(Integer, ForeignKey("orders.id_order"))
    product_id = Column(Integer, ForeignKey("products.id_product"))
    quantity = Column(Integer)
