from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class MovieNation(Base):
    __tablename__ = 'movie_nations'
    
    movie_cd: int = Column(
        'movie_cd',
        Integer,
        ForeignKey('movies.movie_cd'),
        nullable = False
    )
    nation_id: int = Column(
        'nation_id',
        Integer,
        ForeignKey('nations.id'),
        nullable = False
    )
    
    movie = relationship(
        'Movie',
        back_populates = 'movie_genre'
    )
    nation = relationship(
        'Nation',
        back_populates = 'movie_genre'
    )