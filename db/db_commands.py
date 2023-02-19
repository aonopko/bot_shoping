
from models.db_models import Admins, Product


async def get_admin(user_id):
    admins = await Admins.query.where(Admins.id_telegram == user_id).gino.first()
    return admins


async def add_item(**kwargs):
    new_item = await Product(**kwargs).create()
    return new_item


async def del_item(id_product):
    item = await Product.get(id_product)
    await item.delete()


async def get_all_items():
    products = await Product.query.gino.all()
    return products


class UpdateData:
    def __init__(self, id_product, photo=None,
                 price=None, quantity=None):
        self.id_product = id_product
        self.photo = photo
        self.price = price
        self.quantity = quantity

    async def update_db_price(self, id_product, price):
        product = await Product.get(id_product)
        await product.update(price=price).apply()

    async def update_db_photo(self):
        product = await Product.get(self.id_product)
        await product.update(photo=self.photo).apply()

    async def update_db_quantity(self, id_product, quantity):
        product = await Product.get(id_product)
        await product.update(quantity=quantity).apply()
