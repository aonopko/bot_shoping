
from models.db_models import Admins, Product


async def get_admin(user_id):
    admins = await Admins.query.where(Admins.id_telegram == user_id).gino.first()
    return admins


async def add_item(**kwargs):
    new_item = await Product(**kwargs).create()
    return new_item


async def del_item(id_item):
    new_item = await Product.delete.where(id_item == Product.id).gino.status()
    return new_item
