from sqlalchemy import \
    Column, Integer, String, ForeignKey
from backend.config.database_config import Base


class Book(Base):
    __tablename___= 'books'
    
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
        Integer, 
        nullable=False)
    
    url_imagem = Column(
        "url",
        String, 
        nullable=False)

    
    def __init__(self, nome, descricao, valor, url_imagem):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.url_imagem = url_imagem

    