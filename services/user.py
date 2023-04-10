from werkzeug.security import generate_password_hash
from sqlalchemy.orm import Session
from schemas.user import UserSchema
from models.user import User
from database import engine

def create_user(user):
    with Session(engine) as session:
        user['password'] = generate_password_hash(user['password'])
        new_user = User(**user)
        session.add(new_user)
        session.commit()
        return UserSchema(exclude=('created_at', 'id', 'password')).dump(new_user)
