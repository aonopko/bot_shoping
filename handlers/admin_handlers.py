from aiogram.types import Message
from aiogram import Dispatcher
from keyboards.admin_keyboard import admin_menu


async def admin_start(m: Message):
    await m.answer("Меню админа")


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=['admin'],
                                state="*")
