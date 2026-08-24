from fastapi import APIRouter, Depends, HTTPException
from backend.models.admin import Admin
from sqlalchemy.orm import sessionmaker, Session
from backend.config.dependencies import get_session
from backend.config.crypt_config import bcrypt
from backend.schemas.admin_schema import AdminSchema

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/criar-conta")
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

