from sqlalchemy import \
    Column, Integer, String, ForeignKey
from backend.config.database_config import Base

class Admin(Base):
    __tablename___ = 'admin'

    id = Column(
        "id",
        Integer, 
        primary_key=True, 
        autoincrement=True)
    
    username = Column(
        "username",
        String(50), 
        nullable=False, 
        unique=True, 
        index=True)

    email = Column(
        "email",
        String(255), 
        =False, 
        unique=True)

    password = Column(
        "password",
        String(255), 
        nullable=False)

    books = relationship(
        "Book", 
        back_populates="admin"
    )

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password