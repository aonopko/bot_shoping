import loguru
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,\
    CallbackQuery, Message
from aiogram.utils.callback_data import CallbackData

from db.db_commands import add_order_product
from models.db_models import Product




