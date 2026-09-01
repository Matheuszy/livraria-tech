from fastapi import APIRouter, Depends, HTTPException
from backend.config.dependencies import get_session
from sqlalchemy.orm import Session
from backend.models.order import Order
from backend.models.cliente import Cliente
from backend.models.order import Order
from backend.models.book import Book, calcula_total
from backend.config.token_jwt import CheckToken
from backend.schemas.pedido_schema import PedidoSchema

cliente_autenticato = CheckToken(Cliente)

order_router = APIRouter(prefix="/orders", tags=["orders"])


@order_router.get("/my_orders")
async def get_my_orders(
    cliente: Cliente = Depends(cliente_autenticato)
):
    if not cliente.orders:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Nenhum pedido encontrado para este cliente"
        )

    return {
        "cliente": cliente.nome,
        "pedidos": cliente.orders
    }

@order_router.post("/order", status_code=status.HTTP_201_CREATED)
async def post_order(book_id: int, order_schema: PedidoSchema, cliente: Cliente = Depends(cliente_autenticato), session:Session = Depends(get_session)):
    book = session.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Livro não encontrado"
        )

    new_order = Order(
        cliente_id=cliente.id,
        status="EM_ANDAMENTO"
    )

    new_order.books.append(book)
    new_order.calcula_total()

    session.add(new_order)
    session.commit()
    session.refresh(new_order)

    return {
            "message": "Pedido criado com sucesso",
            "pedido_id": new_order.id,
            "valor_total": new_order.valor_total
            }
        
   
    raise HTTPException(status_code=400, detail="Pedido criado")
    
    

@order_router.post("/order/cancel")
async def cancel_order(id_pedido, cliente: Cliente = Depends(cliente_autenticato), session: Session = Depends(get_session)):
    order = session.query(Order).filter(Order.id == id_pedido, 
    Order.cliente_id == client.id).first()

    if not order or cliente.id:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    else:
        oder.status = "CANCELADO"
        session.commit()
        return {
            "message": "Pedido cancelado com sucesso",
            "pedido": order
            }