from aiogram.types import Message
from aiogram import Dispatcher

from keyboards.default.costumer_keyboard import main_menu, categories


async def costumer_start(m: Message):
    await m.answer("Ваше меню", reply_markup=main_menu)


async def socks_button(m: Message):
    await m.answer("Меню", reply_markup=categories)


async def hot_socks(m: Message):
    await m.answer()
    pass


def register_costumer_handlers(dp: Dispatcher):
    dp.register_message_handler(costumer_start, commands=["start"],
                                state="*")
    dp.register_message_handler(socks_button, text=["Каталог"],
                                state="*")
