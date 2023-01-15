from sqlalchemy import Integer, String, Column, DateTime, ForeignKey, E
from sqlalchemy.orm import relationship

from models.base_models import BaseModel, TimedBaseModel


class Customer(BaseModel):
    __tablename__ = "custumer"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    phone = Column(Integer)
    email = Column(String(255))
