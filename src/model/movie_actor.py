from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null

from src.database import Base


class MovieActor(Base):
    __tablename__ = 'movie_actors'
    
    role_name: str = Column(
        'actor_role_name',
        String(length = 16),
        nullable = False
    )
    movie_cd: int = Column(
        'movie_cd',
        Integer,
        ForeignKey('movies.movie_cd'),
        nullable = False
    )
    actor_id: int = Column(
        'actor_id',
        Integer,
        ForeignKey('actors.id'),
        nullable = False
    )
    
    movie = relationship(
        'Movie',
        back_populates = 'movie_actor'
    )
    actor = relationship(
        'Actor',
        back_populates = 'movie_actor'
    )