from pydantic import BaseModel

class ClienteSchema(BaseModel):
    nome = str
    email = str
    password = str
    telefone = str

class ClienteCreate(ClienteSchema):
    pass

class ClienteResponse(BaseModel):
    id = int
    class Config:
        from_attributes = True