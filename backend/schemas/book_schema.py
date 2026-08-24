from pydantic import BaseModel,ConfigDict

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
            model_config = ConfigDict(from_attributes=True)