from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="\U0001f4E6 Додати товар"),
            KeyboardButton(text="\U0001f504 Оновити товар"),
        ],
        [
            KeyboardButton(text="\U0000274C Видалити товар"),
            KeyboardButton(text="Переглянути товар")
        ]
    ],
    resize_keyboard=True
)

update_product = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Фото"),
            KeyboardButton(text="Ціну"),

        ],
        [
            KeyboardButton(text="Кількість"),
            KeyboardButton(text="Додати")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ], resize_keyboard=True
)
