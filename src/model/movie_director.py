from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class MovieDirector(Base):
    __tablename__ = 'movie_directors'
    
    director_id: int =  Column(
        'director_id',
        Integer,
        ForeignKey('directors.id'),
        nullable = False
    )
    movie_cd: int =  Column(
        'movie_cd',
        Integer,
        ForeignKey('movies.movie_cd'),
        nullable = False
    )
    director = relationship(
        'Director',
        back_populates = 'movie_director'
    )
    movie = relationship(
        'Movie',
        back_populates = 'movie_director'
    )