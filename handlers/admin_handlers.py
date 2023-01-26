from aiogram.types import Message
from aiogram import Dispatcher, Bot
from aiogram.types import CallbackQuery

from keyboards.admin_keyboard import admin_menu
from db.db_commands import get_admin
from config_loade import Config, load_config


config: Config = load_config()
bot = Bot(config.bot.token, parse_mode="HTML")
dp = Dispatcher(bot)


async def admin_start(call: CallbackQuery):
    user = call.from_user.id
    if await get_admin(user):
        await call.answer('Привіт адмін')
    else:
        await call.answer('Пока')


def register_admin_handlers(dp: Dispatcher):
    # dp.register_message_handler(admin_start, commands=['admin'], state="*")
    dp.register_callback_query_handler(admin_start, callback=['admin'], state="*")
