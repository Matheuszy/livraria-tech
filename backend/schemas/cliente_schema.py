from pydantic import BaseModel,ConfigDict

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
            model_config = ConfigDict(from_attributes=True)


class LoginSchema(BaseModel):
    email: str
    password: str


    class LoginResponse(BaseModel):
        id: int
        class Config:
            model_config = ConfigDict(from_attributes=True)