from dataclasses import dataclass

@dataclass
class User:
    id: int 
    category_id: str
    alias: str