from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


buy_product = CallbackData("buy", "id_product")


async def buy_button(id_product):
    button = InlineKeyboardButton(text="Купити",
                                  callback_data=buy_product.new(id_product))
    buy_keyboard = InlineKeyboardMarkup()
    buy_keyboard.add(button)
    return buy_keyboard


async def not_paid_kb():
    button = InlineKeyboardButton(text="Оплатит",
                                  callback_data="payment")
    button1 = InlineKeyboardButton(text="Видалити товар",
                                   callback_data="del_payment")
    pay_button = InlineKeyboardMarkup()
    pay_button.add(pay_button, button1)
    return button
