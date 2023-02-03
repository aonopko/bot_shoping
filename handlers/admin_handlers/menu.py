from aiogram import Dispatcher
from aiogram.types import Message

from keyboards.default.admin_keyboard import admin_menu, update_product
from filters.bot_filter import CheckAdmin


async def admin_check(m: Message):
    await m.answer(text="Панель адміна",
                   reply_markup=admin_menu)


async def update_products(m: Message):
    await m.answer(text="Ваше меню для оновлення",
                   reply_markup=update_product)


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_check, CheckAdmin(), commands=["admin"], state="*")
    dp.register_message_handler(update_products, CheckAdmin(), text=["Оновити товар"], state="*")
