from factories import UserFactory
from sqlalchemy import delete
from models import User
from database import db

def seed_up():
    UserFactory().create_many(10)


def seed_down():
    with db.engine.connect() as conn:
        conn.execute(delete(User))
        conn.commit()
