from werkzeug.security import generate_password_hash, check_password_hash
from schemas import UserSchema
from models import User, Role
from database import db

class UserService:
    @staticmethod
    def create_user(**user):
        with db.session() as session:
            user["password"] = generate_password_hash(user["password"])
            role = user.pop("role", "customer")
            roles = session.query(Role).filter(Role.name == role).all()
            new_user = User(**user, roles=roles)
            session.add(new_user)
            session.commit()
            return UserSchema().dump(new_user)


    @staticmethod
    def validate_user(username, password):
        with db.session() as session:
            user = session.query(User).filter(User.username == username).first()
            if user and check_password_hash(user.password, password):
                return UserSchema().dump(user)
