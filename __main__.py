import asyncio
from loguru import logger

from aiogram import Bot, Dispatcher

from config_loade import Config, load_config
from db.base import db_gino
from db.db_commands import get_admin
from handlers.costumer_handlers import register_costumer_handlers
from handlers.admin_handlers import register_admin_handlers


async def main():
    logger.info(f'Bot is loading')
    config: Config = load_config()
    await db_gino.set_bind(f"postgresql://{config.db.user}:{config.db.password}@"
                           f"{config.db.host}/{config.db.db_name}")
    logger.info("Connect to BD")
    bot = Bot(config.bot.token, parse_mode="HTML")
    dp = Dispatcher(bot)
    logger.info("Bot is starting")

    register_costumer_handlers(dp)
    register_admin_handlers(dp)




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
