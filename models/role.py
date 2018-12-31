# coding=utf-8

from sqlalchemy import Column, String, Integer, Date

from base_model import BaseModel


class Actor(BaseModel):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
