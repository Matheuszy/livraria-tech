from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.config.dependencies import get_session
from backend.config.token_jwt import CheckToken
from backend.models.admin import Admin
from backend.models.book import Book
from backend.models.order import Order
from backend.schemas.pedido_schema import PedidoSchema
from backend.schemas.book_schema import BookSchema


check_admin_token = CheckToken(Admin)

admin_book_router = APIRouter(prefix="/admin_books", tags=["admin_books"])

@admin_book_router.get("/all/orders")
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

@admin_book_router.post("/create/book", status_code=status.HTTP_201_CREATED)
async def create_book(
    book: BookSchema,
    admin: Admin = Depends(check_admin_token), 
    session: Session = Depends(get_session) 
):
        new_book = Book(
            nome=book.nome,
            descricao=book.descricao,
            valor=book.valor,
            url_imagem=book.url_imagem,
            admin_id=admin.id
        )

        session.add(new_book)
        session.commit()
        session.refresh(new_book)

        return {
            "message": f"livro criado com sucesso {new_book.nome}"
        }


@admin_book_router.put("/update-book/{id_book}")
async def update_book(
    id_book: int,
    book: BookSchema,
    admin: Admin = Depends(check_admin_token), 
    session: Session = Depends(get_session)
    
):

    exists_book = session.query(Book).filter(Book.id == id_book).first()
    if not exists_book:
        raise HTTPException(
            status_code=400,
            detail="Livro não encontrado"
        )
    
    existing_book.nome = book_schema.nome
    existing_book.descricao = book_schema.descricao
    existing_book.valor = book_schema.valor
    existing_book.url_imagem = book_schema.url_imagem
    existing_book.admin_id = admin.id

    session.commit()
    session.refresh(existing_book)

    return {
        "message": "Livro atualizado com sucesso",
        "book": existing_book
    }



