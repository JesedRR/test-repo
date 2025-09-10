import logging

from app.domain.entities.user import User
from app.external.models.user_model import UserModel
from app.exceptions.exceptions import BusinessException
from app.domain.enums.error_codes import ErrorCode

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserService:
    def __init__(self, db):
        # Sesión de SQLAlchemy (maneja la conexión con la bd)
        self.db = db

    def list_users(self) -> list[User]:
        """
        Get all register users

        return (list[User]): Registered users
        """
        users = self.db.query(UserModel).all() # Crea una consulta sobre la tabla UserModel, y devuleve una lista de objetos UserModel
        userList = [User(id=u.id, name=u.name, last_name=u.last_name,
                    email=u.email, password_hash=u.password_hash, created_at=u.created_at) for u in users]
        return userList

    def create_user(self, user: User) -> bool:
        """
        Create user

        Args:
            User (User): Entity User

        Return (bool): True if user created succesfully, False otherwise
        """
        if not user.name or not user.last_name or not user.email or not user.password_hash:
            logger.warning(f"Missing required fields for user creation: {user}")
            raise BusinessException(ErrorCode.MISSING_FIELDS)

        existing_user = self.db.query(UserModel).filter(UserModel.email == user.email).first()
        if existing_user:
            raise BusinessException(ErrorCode.USER_ALREADY_EXISTS)

        try:
            db_user = UserModel(
                name=user.name,
                last_name=user.last_name,
                email=user.email,
                password_hash=user.password_hash
            )
            self.db.add(db_user)
            self.db.commit()
            self.db.refresh(db_user)
            logger.info(f"User created successfully: {db_user.email}")
            return True
        except Exception as e:
            self.db.rollback()
            logger.error(f"Unexpected error creating user {user.email}: {e}", exc_info=True)
            raise BusinessException(ErrorCode.USER_NOT_CREATED)
        
    def delete_user_by_email(self, email: str) -> bool:
        if not email or not email.strip():
            logger.warning("Missing email for user deletion")
            raise BusinessException(ErrorCode.MISSING_FIELDS)
        
        user = self.db.query(UserModel).filter(UserModel.email == email).first()
        if not user:
            logger.error(f"User not found: {user}")
            raise BusinessException(ErrorCode.USER_NOT_FOUND)
        
        if not isinstance(user, UserModel):
            logger.error(f"User object is not a mapped SQLAlchemy instance: {user}")
            raise BusinessException(ErrorCode.USER_NOT_DELETED)
        
        try:
            self.db.delete(user)
            self.db.commit()
            logger.info(f"User deleted succesfully: {email}")
            return True
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error deleting user {email}: {e}", exc_info=True)
            raise BusinessException(ErrorCode.USER_NOT_DELETED)

