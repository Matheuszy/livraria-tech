from fastapi import FastAPI
from backend.routers.admin import admin_router
from backend.routers.orders import order_router
from backend.routers.login_cliente import login_router


app = FastAPI()
app.include_router(admin_router)
app.include_router(login_router)
app.include_router(order_router)
