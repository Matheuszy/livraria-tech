from sqlalchemy import \
    Column, Integer, String, ForeignKey, Float
from backend.config.database_config import Base
from sqlalchemy.orm import relationship


class Book(Base):
    __tablename__= 'books'
    
    id = Column(
        "id",
        Integer, 
        primary_key=True, 
        autoincrement=True)
    
    nome = Column(
        "nome",
        String(100), 
        nullable=False)
    
    descricao = Column(
        "descricao",
        String(200), 
        nullable=False)
    
    valor = Column(
        "preco",
        Float, 
        nullable=False)
    
    url_imagem = Column(
        "url",
        String, 
        nullable=False)

    admin_id = Column(
        "admin_id",
        Integer, 
    ForeignKey("admins.id"), 
    nullable=True)

    pedido_id = Column(
        "pedido_id", 
        Integer, 
        ForeignKey("orders.id"), 
        nullable=True)

    admin = relationship("Admin", 
    back_populates="books")

    
    def __init__(self, nome, descricao, valor, url_imagem, admin_id=None):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.url_imagem = url_imagem
        self.admin_id = admin_id

    