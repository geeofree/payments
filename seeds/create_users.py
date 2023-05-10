from werkzeug.security import generate_password_hash
from sqlalchemy import delete
from models import User
from database import db
from faker import Faker

fake = Faker()

def create_user():
    return User(username=fake.profile()["username"], password=generate_password_hash("password"))


def seed_up():
    with db.session as session:
        session.add_all([create_user() for _ in range(10)])
        session.commit()


def seed_down():
    with db.engine.connect() as conn:
        conn.execute(delete(User))
        conn.commit()
