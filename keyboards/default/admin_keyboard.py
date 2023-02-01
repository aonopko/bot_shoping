from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Додати товар"),
            KeyboardButton(text="Оновити товар"),
            KeyboardButton(text="Видалити товар")
        ]
    ],
    resize_keyboard=True
)

update_product = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Фото"),
            KeyboardButton(text="Ціну"),
            KeyboardButton(text="Кількість")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ], resize_keyboard=True
)
