import os
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
DB_PORT = os.environ.get("DB_PORT")
DB_HOST = os.environ.get("DB_HOST", "3306")


# Define the MySQL engine using MySQL Connector/Python
engine_setup = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

print(engine_setup)
engine = sqlalchemy.create_engine(
    engine_setup,
    echo=True)

# Define and create the table
Base = declarative_base()

Base.metadata.create_all(engine)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()
