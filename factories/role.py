from .base import Factory
from models import Role

class RoleFactory(Factory):
    def __init__(self):
        self.model = Role


    def define_attributes(self):
        return {
            'name': self.faker().job().replace(' ', '_').lower(),
            'description': self.faker().sentence(nb_words=5),
        }
