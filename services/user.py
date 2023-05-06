from werkzeug.security import generate_password_hash, check_password_hash
from schemas.user import UserSchema
from models.user import User
from database import db

class UserService:
    @staticmethod
    def create_user(user):
        with db.session as session:
            user = user.copy()
            user['password'] = generate_password_hash(user['password'])
            new_user = User(**user)
            session.add(new_user)
            session.commit()
            return UserSchema(exclude=('id', 'password')).dump(new_user)


    @staticmethod
    def validate_user(username, password):
        with db.session as session:
            user = session.query(User).filter(User.username == username).first()
            if user and check_password_hash(user.password, password):
                return UserSchema(exclude=('id', 'password')).dump(user)
