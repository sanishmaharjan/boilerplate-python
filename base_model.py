import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv(verbose=True)
engine = create_engine(os.environ.get('DB_CONNECTION_STRING'))
Session = sessionmaker(bind=engine)

BaseModel = declarative_base()