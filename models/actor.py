# coding=utf-8

from sqlalchemy import Column, String, Integer, Date

from base_model import BaseModel


class Actor(BaseModel):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthday = Column(Date)

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday