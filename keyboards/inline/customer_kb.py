from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from aiogram.types import Message

from states.customers_state import ProductQuantity

buy_product = CallbackData("buy", "id_product")


async def buy_button(id_product):
    await ProductQuantity.quantity.set()
    button = InlineKeyboardButton(text="Купити", callback_data=buy_product.new(id_product))
    buy_keyboard = InlineKeyboardMarkup()
    buy_keyboard.add(button)
    return buy_keyboard

