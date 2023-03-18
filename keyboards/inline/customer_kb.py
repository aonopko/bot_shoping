from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


async def buy_button():
    button = InlineKeyboardButton(text="Купити", callback_data="cust_prom")
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button)
    return keyboard
