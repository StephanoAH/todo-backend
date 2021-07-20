import datetime
from uuid import uuid4

from .db.base import Base
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID


class Todo(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    title = Column(String)
    description = Column(String)
    is_done = Column(Boolean)
    created_on = Column(Date, default=datetime.datetime.now)
    updated_on = Column(
        Date, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
