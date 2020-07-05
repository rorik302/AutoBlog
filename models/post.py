from sqlalchemy import Column, String, Text, LargeBinary

from models.base import Base


class Post(Base):
    title = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    image = Column(LargeBinary)