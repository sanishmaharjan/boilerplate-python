# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base_model import BaseModel


class ContactDetails(BaseModel):
    __tablename__ = 'contact_details'

    id = Column(Integer, primary_key=True)
    phone_number = Column(String)
    address = Column(String)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    actor = relationship("Actor", backref="contact_details")

    def __init__(self, phone_number, address, actor):
        self.phone_number = phone_number
        self.address = address
        self.actor = actor

    def __str__(self):
        return {
            'id': self.id,
            'phone_number' : self.phone_number,
            'address' : self.address,
            'actor_id' : self.actor_id,
            'actor' : self.actor
        }