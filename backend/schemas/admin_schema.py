from pydantic import BaseModel

class AdminSchema(BaseModel):
    username: str
    email: str
    password: str

class AdminCreate(AdminSchema):
    pass

class AdminResponse(AdminSchema):
    id: int
    class Config:
        from_attributes = True