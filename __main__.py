import asyncio
from loguru import logger

from aiogram import Bot, Dispatcher

from config_loade import Config, load_config
from db.base import db_gino
from handlers.costumer import register_costumer
from gino.schema import GinoSchemaVisitor

async def main():
    logger.info(f'Бот завантажується')
    config: Config = load_config()
    await db_gino.set_bind(f"postgresql://{config.db.user}:{config.db.password}@"
                           f"{config.db.host}/{config.db.db_name}")
    db_gino.gino: GinoSchemaVisitor
    await db_gino.gino.create_all()

    # engine = create_async_engine(
    #     f"postgresql+asyncpg://{config.db.user}:{config.db.password}@{config.db.host}/{config.db.db_name}",
    #     future=True
    # )
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    #
    # async_sessionmaker = sessionmaker(
    #     engine, expire_on_commit=False, class_=AsyncSession
    # )


    logger.info("Підключення до БД")
    bot = Bot(config.bot.token, parse_mode="HTML")
    #bot["db"] = async_sessionmaker
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
