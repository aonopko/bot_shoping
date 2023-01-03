from sqlalchemy.orm import declarative_base

Base = declarative_base()
SQLALCHEMY_URL = "postgresql+asyncpg://admin:1983@localhost/adpanel"

