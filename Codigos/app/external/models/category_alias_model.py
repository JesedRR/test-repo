from sqlalchemy import Column, String, Integer, ForeignKey
from app.db import Base

class CategoryAlias(Base):
    __tablename__ = "category_alias"

    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    alias = Column(String, nullable=False)
