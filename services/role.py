from database import db
from models.role import Role
from schemas.role import RoleSchema

class RoleService:
    @staticmethod
    def create_role(role_details):
        with db.session as session:
            new_role = Role(**role_details)
            session.add(new_role)
            session.commit()
            return RoleSchema(exclude=('id',)).dump(new_role)


    @staticmethod
    def find_by_role_name(role_name):
        with db.session as session:
            role = session.query(Role).filter(Role.name == role_name).first()
            if role:
                return RoleSchema(exclude=('id',)).dump(role)
