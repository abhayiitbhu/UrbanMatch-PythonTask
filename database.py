from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import ARRAY
from sqlalchemy.orm import sessionmaker


DATABASE = 'postgresql'
USER = 'home'
PASSWORD = 'root'
HOST = 'localhost'
PORT = '5432'
DB_NAME = 'postgres'

SQLALCHEMY_DATABASE_URL=f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()