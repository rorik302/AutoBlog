from datetime import datetime

from sqlalchemy import Column, String, Text, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship

from project.models import User
from project.models import Base


class Post(Base):
    title = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    image_url = Column(String)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship(User)
    created = Column(DateTime, default=datetime.now())


    def __init__(self, title, text, image_url, user_id):
        self.title = title
        self.text = text
        self.image_url = image_url
        self.user_id = user_id