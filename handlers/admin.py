from aiogram import Dispatcher
from aiogram.types import Message


async def admin_start(m: Message):
    await m.reply("Hello admin")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"],
                                state="*")
