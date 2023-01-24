import asyncio

from aiogram import types, Bot
from sqlalchemy import sql
from db.base import db_gino
from models.db_models import Admins


async def get_admin(user_id):
    admins = await Admins.query.where(Admins.id_telegram == user_id).gino.first()
    return admins
