from pydantic import BaseModel

class BookSchema(BaseModel):
    nome: str
    descricao: str
    valor: int 
    url_imagem: str

class BookCreate(BookSchema):
    pass

class BookResponse(BookSchema):
    id: int
    class Config:
        from_attributes = True