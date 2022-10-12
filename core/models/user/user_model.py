from core.models import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, DefaultClause
from sqlalchemy.sql import func
from sqlalchemy.types import TIMESTAMP, DateTime

class UserModel(Base):
    __tablename__ = "USER"

    user_id = Column("id", Integer, primary_key=True)
    user_name = Column("name", String)
    user_email = Column("email", String)
    user_password = Column("password", String)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_at = Column(DateTime, DefaultClause(func.now()), nullable=True)
    updated_at = Column(DateTime, DefaultClause(func.now(), for_update=True), nullable=True)


