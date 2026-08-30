from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from backend.config.database_config import Base

class Order(Base):

    __tablename__ = "orders"

    id = Column(
        "id",
        Integer,
        primary_key=True,
        autoincrement=True
    )

    # 1. Corrigido para apontar para a tabela 'clientes' e coluna 'id'
    cliente_id = Column(
        "cliente_id",
        Integer,
        ForeignKey("clientes.id"),
        nullable=False
    )

    status = Column(
        "status",
        String
    )

    valor_total = Column(
        "valor_total",
        Float
    )

    cliente = relationship("Cliente", back_populates="orders")

    def __init__(self, cliente_id, status="EM_ANDAMENTO", valor_total=0.0):
        self.cliente_id = cliente_id
        self.status = status
        self.valor_total = valor_total