from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


buy_product = CallbackData("buy", "id_product")
delete_product = CallbackData("del", "id_product")
update_product = CallbackData("update", "id_product")


async def buy_button(id_product):
    button = InlineKeyboardButton(text="Купити",
                                  callback_data=buy_product.new(id_product))
    buy_keyboard = InlineKeyboardMarkup()
    buy_keyboard.add(button)
    return buy_keyboard


async def not_paid_kb(id_product):
    button = InlineKeyboardButton(text="Видалити",
                                  callback_data=delete_product.new(id_product))
    button1 = InlineKeyboardButton(text="Змінити кількість",
                                   callback_data=buy_product.new(id_product))
    pay_button = InlineKeyboardMarkup(row_width=5).row(button).row(button1)
    return pay_button
