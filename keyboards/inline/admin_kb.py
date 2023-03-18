from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.customer_kb import add_callback, delete_callback

add_product = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(
                                               text="Додати",
                                               callback_data=add_callback.new(add_prod="add_item")
                                           ),
                                           InlineKeyboardButton(
                                               text="Скасувати",
                                               callback_data=delete_callback.new(del_prod="del_item")
                                           )
                                       ]
                                   ])
