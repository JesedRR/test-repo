from sqlalchemy import Column, String, Integer
from app.db import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    slug = Column(String, unique=True, nullable=False)
    display_name = Column(String, nullable=False)
    budget_pct_hint = Column(Integer, nullable=True)
