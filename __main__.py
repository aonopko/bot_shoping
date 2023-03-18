import asyncio
from loguru import logger

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from config_loade import Config, load_config
from db.base import db_gino
from handlers.costumer_handlers.handlers import register_costumer_handlers
from handlers.admin_handlers.menu import register_admin_handlers
from handlers.admin_handlers.add_product import register_add_product_handlers
from filters.bot_filter import register_filters
from handlers.admin_handlers.delete_product import register_del_product_hendlers
from handlers.admin_handlers.update_product import register_update_product_hendlers
from handlers.admin_handlers.get_products import register_get_all_items
from handlers.costumer_handlers.man_socks_handler import register_man_socks
from handlers.costumer_handlers.woman_socks_hendlers import register_woman_socks
from handlers.costumer_handlers.child_socks_handlers import register_child_socks


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
    register_del_product_hendlers(dp)
    register_update_product_hendlers(dp)
    register_get_all_items(dp)
    register_man_socks(dp)
    register_woman_socks(dp)
    register_child_socks(dp)

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
