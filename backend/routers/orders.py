from fastapi import APIRouter, Depends, HTTPException
from backend.config.dependencies import get_session
from sqlalchemy.orm import Session
from backend.models.order import Order
from backend.schemas.pedido_schema import PedidoSchema

order_router = APIRouter(prefix="/orders", tags=["orders"])


@order_router.get("/books")
async def get_books():
    return 

@order_router.post("/order")
async def post_order(order_schema: PedidoSchema,session:Session = Depends(get_session)):
    new_order = Order(cliente=PedidoSchema.id_cliente)
    session.add(new_order)
    session.commit()
    return {"message": "Pedido criado com sucesso"}


