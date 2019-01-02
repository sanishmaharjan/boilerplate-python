# coding=utf-8

from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship

from base_model import BaseModel

movies_actors_association = Table(
    'movies_actors', BaseModel.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)


class Movie(BaseModel):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)
    actors = relationship("Actor", secondary=movies_actors_association)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def __str__(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'actors': self.actors
        }