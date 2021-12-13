from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from src.database import Base


class Nation(Base):
    name: str = Column(
        'nation_name',
        String(length = 16),
        nullable = False
    )
    
    movie = relationship(
        'Movie',
        secondary = 'movie_nations',
        back_populates = 'nation'
    )