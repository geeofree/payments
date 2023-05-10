from sqlalchemy import insert
from sqlalchemy.orm import Session
from database import db
from faker import Faker

_fake = Faker()
_factory_session = Session(db.engine, expire_on_commit=False)

class Factory:
    def create(self, **kwargs):
        with _factory_session as session:
            attributes = { **self.define_attributes(), **kwargs }
            new_instance = self.model(**attributes)
            session.add(new_instance)
            session.commit()
            return new_instance


    def create_many(self, count):
        with _factory_session as session:
            results = session.scalars(
                insert(self.model).returning(self.model),
                [self.define_attributes() for _ in range(count)]
            ).all()
            session.commit()
            return results


    def faker(self):
        return _fake
