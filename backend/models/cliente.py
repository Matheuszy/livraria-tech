from sqlalchemy import Column, String, Integer
from backend.config.database_config import Base
from backend.models.valueObjects.endereco import Endereco
from sqlalchemy.orm import composite

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column("id",
                Integer,
                primary_key=True)

    nome_completo = Column(
        "nome",
        String(),
        nullable=False
    )

    age = Column(
        "age",
        Integer,
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

    endereco = composite(
        Endereco,
        Column("rua", String(200)),
        Column("numero", String(200)),
        Column("bairro", String(200)),
        Column("cidade", String(200)),
        Column("estado", String(200)),
        Column("cep", String(200)),
    )

    def __init__(self, nome, age, email, password, telephone, endereco):
        self.nome_completo = nome
        self.age = age
        self.email = email
        self.password = password
        self.telephone = telephone
        self.endereco = endereco