import asyncio
from loguru import logger

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from config_loade import Config, load_config
from db.base import db_gino
from handlers.costumer_handlers.handler import register_costumer_handlers
from handlers.admin_handlers.menu import register_admin_handlers
from handlers.admin_handlers.add_product import register_add_product_handlers
from filters.bot_filter import register_filters


async def main():
    logger.info(f'Bot is loading')
    config: Config = load_config()
    await db_gino.set_bind(f"postgresql://{config.db.user}:{config.db.password}@"
                           f"{config.db.host}/{config.db.db_name}")
    logger.info("Connect to BD")
    storage = RedisStorage2() if config.bot.use_redis else MemoryStorage()
    bot = Bot(config.bot.token, parse_mode="HTML")
    dp = Dispatcher(bot, storage=storage)
    logger.info("Bot is starting")

    register_costumer_handlers(dp)
    register_admin_handlers(dp)
    register_add_product_handlers(dp)
    register_filters(dp)

    try:
        await dp.start_polling()
        logger.info("Disconnect")
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()
        logger.info("Bot is off")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped!")
