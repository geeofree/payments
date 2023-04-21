from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import select
from sqlalchemy.orm import Session
from schemas.user import UserSchema
from models.user import User
from database import db

class UserService:
    @staticmethod
    def create(user):
        with Session(db.engine) as session:
            hashed_password = generate_password_hash(user['password'])
            new_user_payload = { **user, 'password': hashed_password }
            new_user = User(**new_user_payload)
            session.add(new_user)
            session.commit()
            return UserSchema(exclude=('id', 'password', 'created_at')).dump(new_user)

    @staticmethod
    def validate_user(username, password):
        with Session(db.engine) as session:
            user = session.scalars(select(User).where(User.username == username)).first()
            if user and check_password_hash(user.password, password):
                return UserSchema(exclude=('id', 'password')).dump(user)
