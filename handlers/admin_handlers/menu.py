from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from keyboards.default.admin_keyboard import admin_menu, update_product
from filters.bot_filter import CheckAdmin


async def admin_check(m: Message):
    await m.answer(text="Панель адміна",
                   reply_markup=admin_menu)


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_check, CheckAdmin(), commands=["admin"], state="*")
