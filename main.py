from fastapi import FastAPI
from backend.routers.admin import admin_router
from backend.routers.orders import order_router
from backend.routers.login_cliente import login_router
from backend.models.admin import Admin
from backend.models.book import Book
from backend.models.cliente import Cliente
from backend.config.database_config import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(admin_router)
app.include_router(login_router)
app.include_router(order_router)
