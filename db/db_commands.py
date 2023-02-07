
from models.db_models import Admins, Product


async def get_admin(user_id):
    admins = await Admins.query.where(Admins.id_telegram == user_id).gino.first()
    return admins


async def add_item(**kwargs):
    newitem = await Product(**kwargs).create()
    return newitem
