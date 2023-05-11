from factories import UserFactory, RoleFactory
from sqlalchemy import delete
from database import db
from .seeder import Seeder
from .create_roles import _DEFAULT_ROLES
import random

def _get_random_role(roles):
    return { "role": random.choice(roles) }

class CreateRandomUsersSeeder(Seeder):
    @staticmethod
    def seed_up():
        with db.session() as session:
            roles = [role["name"] for role in _DEFAULT_ROLES]
            roles = session.query(RoleFactory.model).filter(RoleFactory.model.name.in_(roles)).all()

        UserFactory()\
            .count(5)\
            .create_each_with(lambda: _get_random_role(roles))


    @staticmethod
    def seed_down():
        with db.session() as session:
            session.execute(delete(UserFactory.model))
            session.commit()
