import datetime
from typing import List
import sqlalchemy as sa

from db.base import db_gino


class BaseModel(db_gino.Model):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_key_columns: List[sa.Column] = table.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


class TimedBaseModel(BaseModel):
    __abstract__ = True

    created_at = db_gino.Column(db_gino.DateTime(True), server_default=db_gino.func.now())
    updated_at = db_gino.Column(
        db_gino.DateTime(True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        server_default=db_gino.func.now(),
    )

