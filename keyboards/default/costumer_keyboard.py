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
            KeyboardButton(text="Теплі"),
            KeyboardButton(text="Літні"),
            KeyboardButton(text="Новорічні")
        ],
        [
            KeyboardButton(text="Новинки"),
            KeyboardButton(text="Акція"),
        ],
        [
            KeyboardButton(text="Назад"),
        ],
    ], resize_keyboard=True
)
