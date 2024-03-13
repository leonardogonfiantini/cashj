from sqlmodel import create_engine, Session
import os 
db_uri = os.environ.get('POSTGRES_URL')

engine = create_engine(
    db_uri
)

SessionLocal = Session(autocommit=False, autoflush=False, bind=engine)