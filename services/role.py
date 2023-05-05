from sqlalchemy import insert, select
from database import db
from models.role import Role
from schemas.role import RoleSchema

class RoleService:
    @staticmethod
    def create_role(role_details):
        with db.engine.connect() as conn:
            new_role = conn.execute(insert(Role).values(**role_details).returning(Role)).first()
            conn.commit()
            return RoleSchema(exclude=('id',)).dump(new_role)


    @staticmethod
    def find_by_role_name(role_name):
        with db.engine.connect() as conn:
            role = conn.execute(select(Role).where(Role.c.name == role_name)).first()
            if role:
                return RoleSchema(exclude=('id',)).dump(role)
