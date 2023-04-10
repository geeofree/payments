from dotenv import dotenv_values
from sqlalchemy import create_engine
dotenv = dotenv_values()
engine = create_engine(dotenv['FLASK_DB_CONNECTION'], echo=True)
