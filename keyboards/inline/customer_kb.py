import loguru
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,\
    CallbackQuery, Message
from aiogram.utils.callback_data import CallbackData

from db.db_commands import add_order_product
from models.db_models import Product


buy_product = CallbackData("buy", "id_product")


async def buy_button(id_product):
    button = InlineKeyboardButton(text="Купити", callback_data=buy_product.new(id_product))
    buy_keyboard = InlineKeyboardMarkup()
    buy_keyboard.add(button)
    return buy_keyboard
