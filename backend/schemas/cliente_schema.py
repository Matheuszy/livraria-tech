from pydantic import BaseModel

class EnderecoSchema(BaseModel):
    rua: str
    numero: str
    bairro: str
    cidade: str
    estado: str
    cep: str


class ClienteSchema(BaseModel):
    nome: str
    age: int
    email: str
    password: str
    telefone: str
    endereco: EnderecoSchema

class ClienteCreate(ClienteSchema):
    pass

class ClienteResponse(BaseModel):
    id: int
    class Config:
        from_attributes = True