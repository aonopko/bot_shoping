from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


buy_product = CallbackData("buy", "id_product")
delete_product = CallbackData("del", "id_product")


async def buy_button(id_product):
    button = InlineKeyboardButton(text="Купити",
                                  callback_data=buy_product.new(id_product))
    buy_keyboard = InlineKeyboardMarkup()
    buy_keyboard.add(button)
    return buy_keyboard


async def not_paid_kb(id_product):
    button = InlineKeyboardButton(text="Видалити товар",
                                  callback_data=delete_product.new(id_product))
    button2 = InlineKeyboardButton(text="1", callback_data="2")
    button3 = InlineKeyboardButton(text="1", callback_data="3")
    button4 = InlineKeyboardButton(text="1", callback_data="4")
    button5 = InlineKeyboardButton(text="1", callback_data="5")
    button1 = InlineKeyboardButton(text="Змінити кількість",
                                   callback_data=buy_product.new(id_product))
    pay_button = InlineKeyboardMarkup(row_width=5).row(button, button2, button3, button4).row(button1)
    return pay_button
