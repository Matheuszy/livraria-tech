from sqlalchemy import \
    Column, Integer, String, ForeignKey
from backend.config.database_config import Base

class Admin(Base):
    __tablename___ = 'admin'

    id = Column(
        Integer, 
        primary_key=True, 
        autoincrement=True)
    
    username = Column(
        String(50), 
        nullable=False, 
        unique=True, 
        index=True)

    email = Column(
        String(255), 
        =False, 
        unique=True)

    password = Column(
        String(255), 
        nullable=False)

    books = relationship(
        "Book", 
        back_populates="admin"
    )