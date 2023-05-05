from sqlalchemy import create_engine, MetaData

class Database:
    def __init__(self):
        self.engine = None
        self.metadata = MetaData()

    def init_engine(self, connection_string):
        if self.engine is None:
            self.engine = create_engine(connection_string)

db = Database()
