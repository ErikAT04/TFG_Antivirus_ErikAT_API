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

def cerate_token(data: dict):
    to_encode = data.copy()
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = db.query(User).filter(and_(User.email == form_data.username, User.passwd == hashlib.sha256(form_data.password.encode()).hexdigest())).first()
    if user:
        token = cerate_token(data={"sub":user.email})
        return {
            "access_token": token,
            "token_type":"bearer"
        }
    
@router.get("/getToken")
def get_token(token:str = Depends(oauth2_scheme)):
    return token

# https://www.youtube.com/watch?v=bYpaPxYgeJ0 