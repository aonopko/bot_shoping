import asyncio
from loguru import logger

from aiogram import Bot, Dispatcher

from config_loade import Config, load_config
from db.base import db_gino
from db.db_commands import add_admin


async def main():
    logger.info(f'Бот завантажується')
    config: Config = load_config()
    await db_gino.set_bind(f"postgresql://{config.db.user}:{config.db.password}@"
                           f"{config.db.host}/{config.db.db_name}")
    logger.info("Підключення до БД")
    bot = Bot(config.bot.token, parse_mode="HTML")
    dp = Dispatcher(bot)
    logger.info("Підключення до БД2")

    try:
        await dp.start_polling()
        logger.info("Бот пішов")
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()
        logger.info("Бот Дойшов")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped!")
