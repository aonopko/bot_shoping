from dotenv import load_dotenv
from dataclasses import dataclass
import os


load_dotenv()


@dataclass
class Bot:
    token: str
    use_redis: bool


@dataclass
class DB:
    host: str
    db_name: str
    user: str
    password: str


@dataclass
class Config:
    bot: Bot
    db: DB


def load_config():
    # Add some checks here?
    return Config(
        bot=Bot(token=os.getenv("BOT_TOKEN"),
                use_redis=bool(os.getenv("USE_REDIS"))),
        db=DB(
            host=os.getenv("DB_HOST"),
            db_name=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS")
        )
    )
