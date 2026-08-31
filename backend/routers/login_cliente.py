from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.config.crypt_config import bcrypt
from backend.config.dependencies import get_session
from backend.schemas.cliente_schema import ClienteSchema, LoginSchema
from backend.models.cliente import Cliente
from backend.models.valueObjects.endereco import Endereco
from backend.config.token_jwt import token_jwt

login_router = APIRouter(prefix="/login", tags=["login"])

@login_router.post("/cliente-cadastro")
async def cliente_cadastro(cliente_schema: ClienteSchema, session: Session = Depends(get_session)):
    cliente = session.query(Cliente).filter(Cliente.email == cliente_schema.email).first()
    if cliente:
        raise HTTPException(status_code=400, detail="E-mail de usuário já cadastrado")
    else:
        novo_endereco = Endereco(rua=cliente_schema.endereco.rua,
                                 numero=cliente_schema.endereco.numero,
                                 bairro=cliente_schema.endereco.bairro,
                                 cidade=cliente_schema.endereco.cidade,
                                 estado=cliente_schema.endereco.estado,
                                 cep=cliente_schema.endereco.cep)
        cript = bcrypt.hash(cliente_schema.password)
        novo_cliente = Cliente(cliente_schema.nome,
                               cliente_schema.age,
                               cliente_schema.email,
                               cript,
                               cliente_schema.telefone,
                               novo_endereco
                               )
        session.add(novo_cliente)
        session.commit()
        return {"message": f"Cliente cadastrado com sucesso {cliente_schema.nome} + {cliente_schema.email}"}

@login_router.post("/logar")
async def logar(login_schema: LoginSchema, session: Session = Depends(get_session)):
    cliente = session.query(Cliente).filter(Cliente.email == login_schema.email).first()
    
    if not cliente or not bcrypt.verify(login_schema.password, cliente.password):
            raise HTTPException(status_code=401, detail="E-mail ou senha incorretos")

    else:
            access_token = token_jwt(cliente.id)
            return {"acess_token": access_token, "token_type": "Bearer"}

