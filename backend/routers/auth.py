from fastapi import APIRouter, Depends, HTTPException
from backend.models.admin import Admin
from sqlalchemy.orm import sessionmaker
from backend.config.dependencies import get_session
from backend.config.crypt_config import crypt_config, bcrypt

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/criar-conta")
async def criar_conta(username: str,email: str, senha: str, session = Depends(get_session)):

    admin = session.query(Admin).filter(Admin.email == email).first()
    if admin:
        return {"message": "Já existe uma conta com esse e-mail"}
    else:
        cript = bcrypt.hash(senha)
        novo_admin = Admin(username, email, cript)
        session.add(novo_admin)
        session.commit()
        session.close()
        return {"message": "Conta criada com sucesso"}

