from datetime import datetime

from sqlalchemy import Column, String, Text, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models import User
from models.base import Base


class Post(Base):
    title = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    image = Column(String)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship(User)
    created = Column(DateTime, default=datetime.now())


    def __init__(self, title, text, image, user_id):
        self.title = title
        self.text = text
        self.image = image
        self.user_id = user_id