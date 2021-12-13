from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from src.database import Base


class Genre(Base):
    name: str = Column(
        'genre_name',
        String(length = 16),
        nullable = False
    )
    
    movie = relationship(
        'Movie',
        secondary = 'movie_genres',
        back_populates = 'genre'
    )