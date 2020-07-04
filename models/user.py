import hashlib

from flask_login import UserMixin
from sqlalchemy import Column, String

from .base import Base


class User(Base, UserMixin):
    username = Column(String, nullable=False, unique=True)
    _password = Column("password", String, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = self.hash_password(value)

    @classmethod
    def hash_password(cls, value):
        return hashlib.sha256(value.encode("utf-8")).hexdigest()

    def __repr__(self):
        return f"User id:{self.id} username:{self.username}"