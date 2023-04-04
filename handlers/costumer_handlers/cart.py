from aiogram.dispatcher import FSMContext
from loguru import logger
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup,\
    CallbackQuery
from aiogram import Dispatcher
from asyncpg.exceptions import UniqueViolationError

from keyboards.default.admin_keyboard import update_product
from keyboards.default.costumer_keyboard import categories
from db.db_commands import get_promotion, get_new_product,\
    add_user, get_item, add_cart
from keyboards.default.costumer_keyboard import main_menu
from keyboards.inline.customer_kb import buy_button, buy_product
from states.customers_state import ProductQuantity





