from sqlalchemy import func, select, insert, delete
from models import Role
from database import db

_DEFAULT_ROLES = [
    { "name": "master", "description": "Manages administrators and system configurations." },
    { "name": "admin", "description": "Manages client users." },
    { "name": "biller", "description": "Manages products" },
    { "name": "customer", "description": "Product consumer." },
]

def seed_up():
   with db.session() as session:
        count_roles_stmt = select(func.count(Role.id)).where(Role.name.in_([role["name"] for role in _DEFAULT_ROLES]))
        (total_roles,) = session.execute(count_roles_stmt).first()

        if total_roles == 0:
            session.execute(insert(Role), _DEFAULT_ROLES)
            session.commit()


def seed_down():
   with db.engine.connect() as conn:
        conn.execute(delete(Role))
        conn.commit()
