from sqlalchemy import Column, String, Integer
from backend.config.database_config import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column("id",
                Integer,
                primary_key=True)

    nome = Column(
        "nome",
        String(200),
        nullable=False
    )

    email = Column(
        "email",
        String(200),
        nullable=False,
        unique=True
    )

    password = Column(
        "password",
        String(200),
        nullable=False,
    )

    telephone = Column(
        "telefone",
        String(200),
        nullable=False,
        unique=True
    )

    def __init__(self, nome, email, password, telephone):
        self.nome = nome
        self.email = email
        self.password = password
        self.telephone = telephone