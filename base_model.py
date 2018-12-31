from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import current_app

engine = create_engine(current_app.config.get('DB_CONNECTION_STRING'))
Session = sessionmaker(bind=engine)

BaseModel = declarative_base()