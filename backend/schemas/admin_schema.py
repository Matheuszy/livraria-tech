from pydantic import BaseModel,ConfigDict

class AdminSchema(BaseModel):
    username: str
    email: str
    password: str

class AdminCreate(AdminSchema):
    pass

class AdminResponse(AdminSchema):
    id: int
    class Config:
        model_config = ConfigDict(from_attributes=True)