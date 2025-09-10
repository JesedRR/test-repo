from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import datetime

from app.domain.entities.user import User

class CreateUserDto(BaseModel):
    name: str = Field(..., min_length=1, description="Name of user")
    last_name: str = Field(..., min_length=1, description="Last name of user")
    email: EmailStr
    password: str = Field(..., min_length=6, description="password must be at least 6 characters")

    @field_validator("name", "last_name", "password")
    def not_empty(cls, v, field):
        if not v or not v.strip():
            raise ValueError(f"{field.name} cannot be empty")
        return v

# de DTO -> entity
def to_entity(user_create: CreateUserDto) -> User:
    return User(
        id=None,
        name=user_create.name,
        last_name=user_create.last_name,
        email=user_create.email,
        password_hash=user_create.password,
        created_at=datetime.now()
    )