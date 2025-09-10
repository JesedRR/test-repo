from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from app.domain.entities.user import User

class GetUserDto(BaseModel):
    id: UUID
    name: str
    last_name: str
    email: str
    created_at: datetime | None

    model_config = ConfigDict(from_attributes=True)




# de entity -> DTO
def from_entity(user: User) -> GetUserDto:
    return GetUserDto(
        id=user.id,
        name=user.name,
        last_name=user.last_name,
        email=user.email,
        created_at=user.created_at  
    )
