from sqlalchemy import func, select, insert, delete
from models import Role, Ability
from database import db
from .seeder import Seeder

_DEFAULT_ABILITIES = [
    { "name": "list_admins", "description": "View all admin accounts." },
    { "name": "view_admin", "description": "View an admin account." },
    { "name": "update_admin", "description": "Update an admin account." },
    { "name": "delete_admin", "description": "Delete an admin account." },
    { "name": "list_billers", "description": "View all biller accounts." },
    { "name": "view_biller", "description": "View a biller account." },
    { "name": "update_biller", "description": "Update a biller account." },
    { "name": "delete_biller", "description": "Delete a biller account." },
    { "name": "list_customers", "description": "View all customer accounts." },
    { "name": "view_customer", "description": "View a customer account." },
    { "name": "update_customer", "description": "Update a customer account." },
    { "name": "delete_customer", "description": "Delete a customer account." },
    { "name": "list_products", "description": "View all products." },
    { "name": "view_product", "description": "View a product." },
    { "name": "update_product", "description": "Update a product." },
    { "name": "delete_product", "description": "Delete a product." },
    { "name": "buy_product", "description": "Buy a product." },
]

_DEFAULT_ROLES = [
    {
        "name": "master",
        "description": "Manages administrators and system configurations.",
        "abilities": ["list_admins", "view_admin", "update_admin", "delete_admin"],
    },
    {
        "name": "admin",
        "description": "Manages client users.",
        "abilities": [
            "list_billers", "view_biller", "update_biller", "delete_biller",
            "list_customers", "view_customer", "update_customer", "delete_customer",
        ],
    },
    {
        "name": "biller",
        "description": "Manages products.",
        "abilities": ["list_products", "view_product", "update_product", "delete_product"],
    },
    {
        "name": "customer",
        "description": "Product consumer.",
        "abilities": ["list_products", "view_product", "buy_product"],
    },
]

class CreateRolesSeeder(Seeder):
    @staticmethod
    def seed_up():
        with db.session() as session:
            abilities = session.scalars(insert(Ability).returning(Ability), _DEFAULT_ABILITIES).all()
            roles = []

            for role in _DEFAULT_ROLES:
                role_abilities = role.pop("abilities")
                filtered_abilities = filter(lambda ability: ability.name in role_abilities, abilities)
                filtered_abilities = list(filtered_abilities)
                role = Role(abilities=filtered_abilities, **role)
                roles.append(role)

            session.add_all(roles)
            session.commit()


    @staticmethod
    def seed_down():
        with db.engine.connect() as conn:
            conn.execute(delete(Ability))
            conn.execute(delete(Role))
            conn.commit()
