from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.database.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.database.models import User
import jwt
import hashlib

from fastapi import APIRouter, Depends

router = APIRouter(prefix="/api", tags=["Token Control"])

oauth2_scheme = OAuth2PasswordBearer("/api/token")

SECRET_KEY = "Clave_Magik_AV"
ALGORITHM = "HS256"

# Función de creación de tokens
def create_token(data: dict):
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm, db:Session = Depends(get_db)):
    pass_encoded = hashlib.sha256(form_data.password.encode()).hexdigest() # Se encripta la contraseña
    user = db.query(User).filter(and_(User.email == form_data.username, User.passwd == pass_encoded)).first()
    if user:
        token = create_token(data={"sub":user.email})
        return {
            "access_token": token,
            "token_type":"bearer"
        }
    
@router.get("/getToken")
def get_token(token:str = Depends(oauth2_scheme)):
    return token 