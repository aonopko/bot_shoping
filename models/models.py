from sqlalchemy import Integer, DateTime, Column

from db.base import Base

class Admin(Base):
    __tablename__ = "administrators"
    id_admin = Column(Integer, primary_key=True, index=True, unique=True)
    id_emploee = Column(Integer)
    date = Column(DateTime)

