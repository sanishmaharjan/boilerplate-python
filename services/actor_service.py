from models import Actor
from base_model import Session


class ActorService:
    @classmethod
    def save(cls, attributes):
        """

        :param attributes:
        :type attributes: dict
        :return:
        """
        actor = Actor(name=attributes.get('name'), birthday=attributes.get('birthday'))
        Session.add(actor)

    @classmethod
    def save_all(cls, attributes_list):
        for attributes in attributes_list:
            actor = Actor(name=attributes.get('name'), birthday=attributes.get('birthday'))
            Session.add(actor)

    @classmethod
    def get_by_id(cls, id, session):
        actor = session.query(Actor).filter_by(id=id).first()
        return actor
