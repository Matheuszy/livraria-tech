from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.config.dependencies import get_session
from backend.config.token_jwt import CheckToken
from backend.models.admin import Admin
from backend.models.book import Book
from backend.models.cliente import Cliente
from backend.models.order import Order
from backend.schemas.pedido_schema import PedidoSchema


cliente_autenticato = CheckToken(Cliente)
check_admin_token = CheckToken(Admin)

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
async def post_order(
    book_id: int, 
    order_schema: PedidoSchema, 
    cliente: Cliente = Depends(cliente_autenticato), 
    session: Session = Depends(get_session)
):
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


@order_router.post("/order/cancel")
async def cancel_order(
    id_pedido: int, 
    cliente: Cliente = Depends(cliente_autenticato), 
    session: Session = Depends(get_session)
):
    order = session.query(Order).filter(
        Order.id == id_pedido, 
        Order.cliente_id == cliente.id
    ).first()

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Pedido não encontrado ou não pertence a este usuário"
        )

    order.status = "CANCELADO"
    session.commit()
    session.refresh(order)

    return {
        "message": "Pedido cancelado com sucesso",
        "pedido": order
    }


# --- ROTA: Listar Todos os Pedidos (Apenas Admin) ---
@order_router.get("/all/orders")
async def all_orders(
    page: int = Query(1, ge=1, description="Número da página"),
    limit: int = Query(50, le=100, description="Quantidade de registros por página"),
    admin: Admin = Depends(check_admin_token), 
    session: Session = Depends(get_session)
):

    offset_value = (page - 1) * limit
    total_orders = session.query(Order).count()

    orders = (
        session.query(Order)
        .order_by(Order.id.desc())
        .offset(offset_value)
        .limit(limit)
        .all()
    )

    return {
        "page": page,
        "limit": limit,
        "total_records": total_orders,
        "total_pages": (total_orders + limit - 1),
        "orders": orders
    }