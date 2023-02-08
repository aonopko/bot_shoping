from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="Шкарпетки"),
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
            KeyboardButton(text="Зимові"),
            KeyboardButton(text="Літні"),
        ],
        [
            KeyboardButton(text="Демісезонні"),
            KeyboardButton(text="Новинки"),
        ],
        [
            KeyboardButton(text="Назад"),
        ],
    ], resize_keyboard=True
)
