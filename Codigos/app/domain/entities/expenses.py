from uuid import UUID, uuid4
from datetime import date, datetime
from dataclasses import dataclass

@dataclass
class Expense:
        id = int | None
        user_id = int
        amount_cents = float
        expense_date = datetime
        note = str | None = None
        raw_text = str | None = None
        audio_url = str | None = None
        category_id = int | None = None
        category_model_score = float | None = None
        status = str | None = None
        created_at = datetime | None = None
