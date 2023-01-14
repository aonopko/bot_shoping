from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from config_loade import Config, load_config
from db.core import db_gino

config_env: Config = load_config()

connect = f"postgresql://{config_env.db.user}:{config_env.db.password}@" \
          f"{config_env.db.host}/{config_env.db.db_name}"

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)
target_metadata = db_gino
config.set_main_option("sqlalchemy.url", connect)


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
