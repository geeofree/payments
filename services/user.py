from sqlalchemy.orm import Session
from database import engine
from models.user import User

def create_user(user):
    with Session(engine) as session:
        new_user = User(**user)
        session.add(new_user)
        session.commit()
        return new_user
