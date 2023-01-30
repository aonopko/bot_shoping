from aiogram import Dispatcher
from aiogram.types import Message

from db.db_commands import get_admin
from keyboards.default.admin_keyboard import admin_menu, update_product


async def admin_check(m: Message):
    user = m.from_user.id
    if await get_admin(user):
        await m.answer(text="Привіт Адмін",
                       reply_markup=admin_menu)
    else:
        await m.answer('Ви не Адмін')


async def update_products(m: Message):
    await m.answer(text="Ваше меню для оновлення",
                   reply_markup=update_product)


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_check, commands=["admin"], state="*")
    dp.register_message_handler(update_products, text=["Оновити товар"], state="*")
