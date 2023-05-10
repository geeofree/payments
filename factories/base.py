from utils.exceptions import NonPositiveException
from sqlalchemy import insert
from database import db
from faker import Faker

_fake = Faker()

class Factory:
    def __new__(cls, **kwargs):
        new_instance = super().__new__(cls)
        new_instance._model = cls.model
        return new_instance


    def __init__(self, **kwargs):
        self.faker = _fake
        self._options = kwargs
        self._count = 1
        self._attached = None


    def count(self, count):
        if count < 1:
            raise NonPositiveException("Count must be a positive integer. Received {}".format(count))
        self._count = count
        return self


    def attach(self, **kwargs):
        self._attached = kwargs
        return self


    def create(self, **kwargs):
        with db.session(expire_on_commit=False) as session:
            attributes = self.define_attributes()

            if self._count < 2:
                record = self._model(**self._get_attributes(**kwargs))
                session.add(record)
                session.commit()
                return record

            optimized = self._options.get("optimize_bulk_inserts", False)

            if optimized:
                records = session.execute(insert(self._model), [self.define_attributes() for _ in range(self._count)])
                session.commit()
                return

            records = [self._model(**self._get_attributes(**kwargs)) for _ in range(self._count)]
            session.add_all(records)
            session.commit()
            return records


    def _get_attributes(self, **kwargs):
        attributes = { **self.define_attributes(), **kwargs }
        if self._attached is not None:
            attributes = { **self._attached, **attributes }
        return attributes
