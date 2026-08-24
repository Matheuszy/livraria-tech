from sqlalchemy import \
    Column, Integer, String, ForeignKey, Float
from backend.config.database_config import Base

class Order(Base):

    __tablename__ = "orders"

    id = Column(
        "id",
        Integer,
        primary_key=True,
        autoincrement=True
    )

    cliente = Column(
        "cliente",
        Integer,
        ForeignKey("cliente_id")
    )

    status = Column(
        "status",
        String
    )

    valor_total = Column(
        "valor_total",
        Float
    )

    def __init__(self, cliente, status="EM_ANDAMENTO", valor_total=0.0):
        self.cliente = cliente
        self.status = status
        self.valor_total = valor_total