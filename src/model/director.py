from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from src.database import Base


class Director(Base):
    name: str = Column(
        'director_name',
        String,
        nullable = False
    )
    movie = relationship(
        'Movie',
        secondary = 'movie_directors',
        back_populates = 'director'
    )
    