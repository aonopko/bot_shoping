from aiogram.types import Message
from aiogram import Dispatcher, Bot
from aiogram.dispatcher.filters import Command

from keyboards.costumer_keyboard import main_menu, categories

from config_loade import Config, load_config


config: Config = load_config()
bot = Bot(config.bot.token, parse_mode="HTML")
dp = Dispatcher(bot)


@dp.message_handler(text="start")
async def costumer_start(m: Message):
    await m.answer("Ваше меню", reply_markup=main_menu)


async def socks_button(m: Message):
    await m.answer("Меню", reply_markup=categories)


# def register_costumer_handlers(dp: Dispatcher):
#     dp.register_message_handler(costumer_start, commands=["start"],
#                                 state="*")
#     dp.register_message_handler(socks_button, text=["Шкарпетки"],
#                                 state="*")
