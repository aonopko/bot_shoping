
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


async def update_db_photo(id_product, photo):
    product = await Product.get(id_product)
    await product.update(photo=photo).apply()
