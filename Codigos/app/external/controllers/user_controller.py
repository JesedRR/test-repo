from fastapi import APIRouter, Depends, Query
from pydantic import EmailStr
from app.db import get_db
from app.domain.services.user_service import UserService
from app.external.dtos.get_user_dto import GetUserDto, from_entity
from app.external.dtos.create_user_dto import CreateUserDto, to_entity

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}, 400: {"description": "Bad request"}}
)

@router.get("/", response_model=list[GetUserDto], summary="Get all users", description="Retrieve a list of all registered users")
def get_users(db=Depends(get_db)):
    service = UserService(db)
    return [from_entity(u) for u in service.list_users()]

@router.post("/", response_model=bool, summary="Create a new user", description="Create a new user with required fields")
def create_user(user_create: CreateUserDto, db=Depends(get_db)):
    service = UserService(db)
    return service.create_user(to_entity(user_create))

@router.delete("/", response_model=bool, summary="Delete user by email", description="Delete a user by providing their email address")
def delete_user(email: EmailStr = Query(..., description="Email of the user to delete"), db=Depends(get_db)):
    service = UserService(db)
    return service.delete_user_by_email(email)
