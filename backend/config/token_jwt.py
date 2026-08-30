from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os

load_dotenv()

ALGORITH = os.getenv("ALGORITH")
ACESS_TOKEN_MIN = os.getenv("ACESS_TOKEN_MIN")

SECRET_KEY = os.getenv("SECRET_KEY")

def token_jwt(id_cliente):
    data_expira = datetime.now(timezone.utc) + timedelta(minutes=int(ACESS_TOKEN_MIN))
    dic_info = {"sub": id_cliente, "exp": data_expira}
    jtw_encode = jwt.encode(dic_info, SECRET_KEY, ALGORITH)
    return jtw_encode

