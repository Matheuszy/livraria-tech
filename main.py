from fastapi import FastAPI
from backend.routers.auth import auth_router
from backend.routers.orders import order_router
from backend.routers.login_cliente import login_router


app = FastAPI()
app.include_router(auth_router)
app.include_router(login_router)
app.include_router(order_router)
