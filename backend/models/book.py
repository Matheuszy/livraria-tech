from sqlalchemy import \
    Column, Integer, String, ForeignKey
from backend.config.database_config import Base


class Book(Base):
    __tablename___= 'books'
    id = Column(Integer, primary_key=true, index=true)
    