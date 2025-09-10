from enum import Enum

class ErrorCode(Enum):
    # General
    MISSING_FIELDS = "Required fields are missing"

    # User
    USER_NOT_FOUND = "User not found"
    USER_ALREADY_EXISTS = "User already exists"
    USER_NOT_CREATED = "User could not be created"
    USER_NOT_DELETED = "User could not be deleted"
