from sqlalchemy import delete
from models import Role
from database import db

def seed_up():
   with db.session as session:
        session.add_all([
            Role(name="master", description="Manages administrators and system configurations."),
            Role(name="admin", description="Manages client users."),
            Role(name="biller", description="Manages products"),
            Role(name="customer", description="Product consumer."),
        ])
        session.commit()


def seed_down():
   with db.engine.connect() as conn:
        conn.execute(delete(Role))
        conn.commit()
