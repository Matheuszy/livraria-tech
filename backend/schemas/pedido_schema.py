from pydantic import BaseModel,ConfigDict

class PedidoSchema(BaseModel):
    cliente: int
    
class PedidoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)