from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="\U0001f4E6 Додати товар"),
            KeyboardButton(text="\U0001f504 Оновити товар"),
        ],
        [
            KeyboardButton(text="\U0000274C Видалити товар"),
        ],
        [
            KeyboardButton(text="Знайти товар по id"),
            KeyboardButton(text="Знайти товар по фото")
        ]
    ],
    resize_keyboard=True
)

update_product = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="\U0001F4F7 Фото"),
            KeyboardButton(text="\U0001F4C8 Ціну"),

        ],
        [
            KeyboardButton(text="\U0001F4CA Кількість"),
            KeyboardButton(text="Акція")
        ],
        [
            KeyboardButton(text="Додати Новінку"),
            KeyboardButton(text="\U0001F194 Додати id")
        ],
        [
            KeyboardButton(text="\U000025C0 Назад")
        ]
    ], resize_keyboard=True
)
