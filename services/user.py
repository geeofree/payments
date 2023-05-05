from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import select, insert
from schemas.user import UserSchema
from models.user import User
from database import db

class UserService:
    @staticmethod
    def create(user):
        with db.engine.connect() as conn:
            user = user.copy()
            user['password'] = generate_password_hash(user['password'])
            new_user = conn.execute(insert(User).values(**user).returning(User)).first()
            conn.commit()
            return UserSchema(exclude=('id', 'password')).dump(new_user)

    @staticmethod
    def validate_user(username, password):
        with db.engine.connect() as conn:
            user = conn.execute(select(User).where(User.c.username == username)).first()
            if user and check_password_hash(user.password, password):
                return UserSchema(exclude=('id', 'password')).dump(user)
