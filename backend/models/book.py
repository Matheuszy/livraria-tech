from sqlalchemy import \
    Column, Integer, String, ForeignKey
from backend.config.database_config import Base


class Book(Base):
    __tablename___= 'books'
    id = Column(Integer, primary_key=true, index=true)
    nome = Column(String(100), nullable=false)
    descricao = Column(String(200), nullable=false)
    valor = Column(Integer, nullable=false)
    url_imagem = Column(String, nullable=false)

    