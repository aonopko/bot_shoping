from operator import and_

from models.db_models import Admins, Product, Customer


async def get_admin(user_id):
    admins = await Admins.query.where(Admins.id_telegram == user_id).gino.first()
    return admins


async def add_item(**kwargs):
    new_item = await Product(**kwargs).create()
    return new_item


async def add_user(**kwargs):
    user = await Customer(**kwargs).create()
    return user


async def del_item(id_product):
    item = await Product.get(id_product)
    await item.delete()


async def get_item(id_product):
    item = await Product.query.where(Product.id_product == id_product).gino.first()
    return item


async def get_all_items():
    product = await Product.query.gino.all()
    return product


async def get_all_photo():
    photo = await Product.query.where(Product.photo == Product.photo).gino.all()
    return photo


async def update_db_promotion(id_product, promotion):
    product = await Product.get(id_product)
    await product.update(promotion=promotion).apply()


async def delete_promotion(id_product):
    product = await Product.get(id_product)
    await product.update(promotion=None).apply()


async def update_db_new_item(id_product, new_product):
    product = await Product.get(id_product)
    await product.update(new_product=new_product).apply()


async def delete_new_item(id_product):
    product = await Product.get(id_product)
    await product.update(new_product=None).apply()


async def get_promotion():
    promotion = await Product.query.where(Product.promotion == Product.promotion).gino.all()
    return promotion


async def get_new_product():
    new_product = await Product.query.where(Product.new_product == Product.new_product).gino.all()
    return new_product


async def get_socks(category_code: str, sub_category_code: str):
    hot_man_socks = await Product.query.where(and_(
        Product.category_code == category_code,
        Product.sub_category_code == sub_category_code)).gino.all()
    return hot_man_socks


class UpdateData:
    def __init__(self, id_product, photo=None,
                 price=None, quantity=None, promotion=None):
        self.id_product = id_product
        self.photo = photo
        self.price = price
        self.quantity = quantity
        self.promotion = promotion

    async def update_db_price(self, id_product, price):
        product = await Product.get(id_product)
        await product.update(price=price).apply()

    async def update_db_photo(self):
        product = await Product.get(self.id_product)
        await product.update(photo=self.photo).apply()

    async def update_db_quantity(self, id_product, quantity):
        product = await Product.get(id_product)
        await product.update(quantity=quantity).apply()
