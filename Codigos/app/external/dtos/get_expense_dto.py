from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import date, datetime
from app.domain.entities.expenses import Expense

class GetExpenseDto(BaseModel):
    id: UUID
    user_id: int
    amount: float
    expense_date: date
    note: str
    raw_text: str
    audio_url: str
    category_id: int
    category_model_score: float
    status: str
    created_at: datetime | None

    model_config = ConfigDict(from_attributes=True)




# de entity -> DTO
def from_entity(expense: Expense) -> GetExpenseDto:
    return GetExpenseDto(
        id=expense.id,
        user_id=expense.user_id,
        expense_date=expense.expense_date,
        note=expense.note,
        raw_text=expense.raw_text,
        audio_url=expense.audio_url,
        category_id=expense.category_id,
        category_model_score=expense.category_model_score,
        status=expense.status,
        created_at=expense.created_at  
    )
