from pydantic import BaseModel, Field, field_validator
from datetime import date, datetime
from typing import Optional

from app.domain.entities.expenses import Expense

class CreateExpenseDto(BaseModel):
    amount: float = Field(..., gt=0, description="Amount of the expense in Mexican Pesos (MXN)")
    expense_date: Optional[date] = Field(
        None, description="Date of the expense. Defaults to today if not provided"
    )
    note: Optional[str] = Field(None, description="Optional notes about the expense")
    raw_text: str = Field(..., min_length=1, description="Description or text of the expense for automatic categorization")
    category_id: Optional[int] = Field(
        None, description="ID of the assigned category. Can be automatically determined if omitted"
    )
    status: Optional[str] = Field(
        "pending", description="Expense status: 'pending' if categorization is needed, 'processed' if category is assigned"
    )

    @field_validator("name", "last_name", "password")
    def not_empty(cls, v, field):
        if not v or not v.strip():
            raise ValueError(f"{field.name} cannot be empty")
        return v

# de DTO -> entity
def to_entity(expense: CreateExpenseDto) -> Expense:
    return Expense(
        id=None,
        name=user_create.name,
        last_name=user_create.last_name,
        email=user_create.email,
        password_hash=user_create.password,
        created_at=datetime.now()
    )