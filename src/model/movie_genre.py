from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class MovieGenre(Base):
    __tablename__ = 'movie_genres'
    
    movie_cd: int = Column(
        'movie_cd',
        Integer,
        ForeignKey('movies.movie_cd'),
        nullable = False
    )
    genre_id: int = Column(
        'genre_id',
        Integer,
        ForeignKey('genres.id'),
        nullable = False
    )
    
    movie = relationship(
        'Movie',
        back_populates = 'movie_genre'
    )
    genre = relationship(
        'Genre',
        back_populates = 'movie_genre'
    )