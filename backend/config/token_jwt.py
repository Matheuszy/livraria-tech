import os
from typing import Type, TypeVar
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from backend.config.dependencies import get_session
from backend.config.database_config import Base

load_dotenv()

ALGORITH = os.getenv("ALGORITH")
ACESS_TOKEN_MIN = os.getenv("ACESS_TOKEN_MIN")
SECRET_KEY = os.getenv("SECRET_KEY")

security = HTTPBearer()

T = TypeVar("T", bound=Base)

def token_jwt(id_user, duracao=timedelta(minutes=int(ACESS_TOKEN_MIN))):
    data_expira = datetime.now(timezone.utc) + duracao
    dic_info = {"sub": str(id_user), "exp": data_expira}
    jtw_encode = jwt.encode(dic_info, SECRET_KEY, ALGORITH)
    return jtw_encode

def verify_token(token: str, model: Type[T], db: Session) -> T:
    exception_unauthorized = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido ou expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITH])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise exception_unauthorized
    except JWTError:
        raise exception_unauthorized

    
    entity = db.query(model).filter(model.id == int(user_id)).first()
    if not entity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"{model.__name__} não encontrado"
        )
        
    return entity


class CheckToken:
    def __init__(self, model: Type[T]):
        self.model = model

    def __call__(
        self, 
        credentials: HTTPAuthorizationCredentials = Depends(security), 
        db: Session = Depends(get_session)
    ) -> T:
        token = credentials.credentials
        return verify_token(token, self.model, db)