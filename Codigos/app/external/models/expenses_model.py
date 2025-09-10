from sqlalchemy import Column, String, Float, Integer, Date, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from app.db import Base

class Expenses(Base):
    __tablename__ = "expenses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    amount = Column(Float, nullable=False)
    expense_date = Column(Date, nullable=False, server_default=func.current_date())
    note = Column(String, nullable=True)
    raw_text = Column(String, nullable=True)
    audio_url = Column(String, nullable=True)
    category_id = Column(Integer, nullable=True)
    category_model_score = Column(float, nullable=True)
    status = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())