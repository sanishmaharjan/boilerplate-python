# coding=utf-8

from sqlalchemy import Column, String, Integer, Date

from base_model import BaseModel


class Role(BaseModel):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return {
            'id': self.id,
            'name': self.name,
        }
