from pydantic import BaseModel,ConfigDict

class PedidoSchema(BaseModel):
    id_cliente: int
    
class PedidoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)