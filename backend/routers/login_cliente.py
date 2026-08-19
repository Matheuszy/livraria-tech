from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import sessionmaker
from backend.config.crypt_config import crypt_config, bcrypt
from backend.config.dependencies import get_session
from backend.schemas.cliente_schema import ClienteSchema
from backend.config.database_config import crypt_config, bcrypt
from backend.models.cliente import Cliente

login_router = APIRouter(prefix="/login", tags=["login"])

@login_router.post("/cliente-cadastro")
async def cliente_cadastro(cliente_schema : ClienteSchema, session = Depends(get_session)):
    cliente = session.query(models.Cliente).filter(models.Cliente.email == cliente_schema.email).first()
    if not cliente:
        raise HTTPException(status_code=400, detail="E-mail de usuário não cadastrado")
    else:
        cript = bcrypt.hash(cliente_schema.password)
        novo_cliente = Cliente(cliente_schema.nome, cliente_schema.email, cript, cliente_schema.telefone)
        session.add(novo_cliente)
        session.commit()
        return {"message": f"Cliente cadastrado com sucesso {cliente_schema.nome} + {cliente_schema.email}"}
