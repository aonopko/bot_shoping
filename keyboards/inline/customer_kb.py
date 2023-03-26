import loguru
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,\
    CallbackQuery, Message
from db.db_commands import add_order_product


async def buy_button():
    button = InlineKeyboardButton(text="Купити", callback_data="cust_prom")
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button)
    return keyboard
