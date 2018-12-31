from enum import Enum


class RoleEnum(Enum):
    """
        Role Enum.
    """

    USER = (1, 'user')
    ADMIN = (2, 'admin')
    GUEST = (3, 'guest')

    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
