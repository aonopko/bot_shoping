from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from base_models import BaseModel, TimedBaseModel


class BSModel(BaseModel):
    __tablename__ = "bsmodel"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
