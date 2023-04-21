from sqlalchemy import create_engine

class Database:
    engine = None

    def init_engine(self, connection_string):
        if self.engine is None:
            self.engine = create_engine(connection_string)

db = Database()
