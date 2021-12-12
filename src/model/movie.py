from datetime import datetime
from sqlalchemy import Integer, Column, String, DateTime, Boolean
from sqlalchemy.orm import relation

from src.database import Base


class Movie(Base):
    id : int = Column(
        'movie_cd',
        Integer,
        primary_key = True,
        autoincrement = True
    )
    name: str = Column(
        'movie_name',
        String(length = 64),
        nullable = False
    )
    released_date: datetime = Column(
        'movie_released_date',
        DateTime(timezone = True),
        nullable = False
    )
    image: str = Column(
        'movie_image',
        String(length =  1024),
        nullable = False
    )
    total_audiences: int = Column(
        'movie_total_autidences',
        Integer,
        nullable = False
    )
    is_only_seoul: bool = Column(
        'is_only_seoul',
        Boolean,
        nullable = False,
        default = False
    )
    
    