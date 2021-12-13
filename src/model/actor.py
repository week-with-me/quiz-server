from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from src.database import Base


class Actor(Base):
    name: str = Column(
        'actor_name',
        String(length = 64),
        nullable = False
    )

    movie = relationship(
        'Movie',
        secondary = 'movie_actors',
        back_populates = 'actor'
    )