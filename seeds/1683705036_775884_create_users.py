from werkzeug.security import generate_password_hash
from sqlalchemy import insert, delete
from models import User
from database import db
from faker import Faker

fake = Faker()

def get_random_user():
    return { 'username': fake.profile()["username"], 'password': generate_password_hash("password") }


def seed_up():
    with db.session as session:
        session.execute(insert(User), [get_random_user() for _ in range(10)])
        session.commit()


def seed_down():
    with db.engine.connect() as conn:
        conn.execute(delete(User))
        conn.commit()
