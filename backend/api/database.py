from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

import os 
db_uri = os.environ.get('POSTGRES_URL')

engine = create_engine(
    db_uri
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()