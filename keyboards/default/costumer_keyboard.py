from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Каталог"),
            KeyboardButton(text="Кошик")
        ],
        [
            KeyboardButton(text="Відгуки"),
            KeyboardButton(text="Доставка")
        ],
    ],
    resize_keyboard=True
)

categories = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="\U000026C4 Теплі"),
            KeyboardButton(text="\U00002600 Літні"),
            KeyboardButton(text="\U00002744 Новорічні")
        ],
        [
            KeyboardButton(text="\U0001f195 Новинки"),
            KeyboardButton(text="\U0001F48E Акція"),
        ],
        [
            KeyboardButton(text="\U000021A9 Назад"),
        ],
    ], resize_keyboard=True
)

cart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Оплочені замовлення"),
            KeyboardButton(text="Ваше замовлення")
        ],
        [
            KeyboardButton(text="Назад"),
        ],
    ], resize_keyboard=True
)
