from fastapi import APIRouter, Depends, HTTPException
from backend.models.admin import Admin
from sqlalchemy.orm import sessionmaker, Session
from backend.config.dependencies import get_session
from datetime import datetime, timedelta, timezone
from backend.config.crypt_config import bcrypt
from backend.config.token_jwt import check_token
from backend.schemas.admin_schema import AdminSchema, LoginAdmin

admin_router = APIRouter(prefix="/auth", tags=["auth"])

@admin_router.post("/criar-conta")
async def criar_conta(admin_schema: AdminSchema, session:Session = Depends(get_session)):

    admin = session.query(Admin).filter(Admin.email == admin_schema.email).first()
    if admin:
        raise HTTPException(status_code=400, detail="E-mail de usuário já cadastrado")
    else:
        cript = bcrypt.hash(admin_schema.password)
        novo_admin = Admin(admin_schema.username, admin_schema.email, cript)
        session.add(novo_admin)
        session.commit()
        return {"message": f"Conta criada com sucesso {novo_admin.email}"}

@admin_router.post("/admin/logar")
async def login_admin(admin_login: LoginAdmin, session: Session = Depends(get_session)):
    admin = session.query(Admin).filter(Admin.email == admin_login.email).first()

    if not admin or not bcrypt.verify(admin_login.password, admin.password):
        raise HTTPException(status_code=401, detail="E-mail ou senha incorretos")
    else:
        access_token = token_jwt(admin.id)
        refresh_token = token_jwt(admin.id, duracao=timedelta(days=15))
        return {
            "acess_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer"}

@admin_auth_router.get("/refresh_token_admin")
async def refresh_token(token):
    admin = check_token(token)
    acess_token = token_jwt(admin.id)
    return {
        "acess_token": acess_token,
        "token_type": "Bearer"
    }
