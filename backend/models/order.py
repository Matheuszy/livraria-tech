from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from backend.config.database_config import Base
from backend.models.book import Book

class Order(Base):

    __tablename__ = "orders"

    id = Column(
        "id",
        Integer,
        primary_key=True,
        autoincrement=True
    )

    cliente_id = Column(
        "cliente_id",
        Integer,
        ForeignKey("clientes.id"),
        nullable=False
    )

    books: List[Book] = relationship(
        "Book", 
        backref="pedido", 
        cascade="all, delete-orphan")

    status = Column(
        "status",
        String
    )

    valor_total = Column(
        "valor_total",
        Float
    )

    cliente = relationship("Cliente", back_populates="orders")

    def calcula_total(self):
        self.valor_total = sum(book.valor for book in self.books )
        return self.valor_total

    def __init__(self, cliente_id, status="EM_ANDAMENTO", valor_total=0.0):
        self.cliente_id = cliente_id
        self.status = status
        self.valor_total = valor_total