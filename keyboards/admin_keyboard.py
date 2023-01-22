from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Додати товар"),
            KeyboardButton(text="Видалити товар")
        ],
        [
            KeyboardButton(text="Відгуки"),
            KeyboardButton(text="Доставка")
        ],
    ],
    resize_keyboard=True
)
