from .factory import Factory
from models import Role

class RoleFactory(Factory):
    model = Role

    def define_attributes(self):
        return {
            'name': self.faker.job().replace(' ', '_').lower(),
            'description': self.faker.sentence(nb_words=5),
        }
