from dataclasses import dataclass

@dataclass
class Categories:
    id: int 
    slug: str
    display_name: str
    budget_pct_hint: str | None = None