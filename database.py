from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

class Database:
    def __init__(self):
        self.engine = None
        self.session = None
        self.metadata = MetaData()


    def init_engine(self, connection_string, **kwargs):
        if self.engine is None:
            self.engine = create_engine(connection_string, **kwargs)
            self.session = sessionmaker(self.engine)


db = Database()
