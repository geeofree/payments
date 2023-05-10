from sqlalchemy import insert
from database import db
from faker import Faker

_fake = Faker()

class Factory:
    def __init__(self):
        self.fake = Faker()


    def create(self, **kwargs):
        with db.session as session:
            attributes = { **self.define_attributes(), **kwargs }
            new_instance = self.model(**attributes)
            session.add(new_instance)
            session.commit()
            session.refresh(new_instance)
            return new_instance


    def create_many(self, count):
        with db.session as session:
            results = session.scalars(
                insert(self.model).returning(self.model),
                [self.define_attributes() for _ in range(count)]
            ).all()
            session.commit()
            [session.refresh(result) for result in results]
            return results


    def faker(self):
        return _fake
