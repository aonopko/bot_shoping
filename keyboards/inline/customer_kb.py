from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,\
    CallbackQuery
from db.db_commands import add_order_product


async def buy_button(id_product):
    product_id = {"product_id": id_product}
    await add_order_product(**product_id)
    button = InlineKeyboardButton(text="Купити", callback_data="cust_prom")
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button)
    return keyboard
