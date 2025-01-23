from fastapi import APIRouter, Depends
from app.repository import Schemas
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database import models

router = APIRouter(prefix="/api/users")

@router.get("/")
def get_all_users(db:Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.get("/{string}")
def get_user_by_email_or_username(string:str, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == string or models.User.username == string).first()
    if user:
        return user
    else:
        raise Exception("Error: Usuario no encontrado")
    
@router.post("/insert")
def create_user(user:Schemas.User, db:Session = Depends(get_db)):
    usuario = models.User()
    usuario.email = user.email
    usuario.username = user.username
    usuario.passwd = user.passwd
    usuario.image = user.image
    db.add(usuario)
    db.commit()
    return usuario

@router.put("/{email}/update")
def update_user(email:str, user:Schemas.User, db:Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.email == email).first()
    if usuario:
        usuario.email = user.email
        usuario.passwd = user.passwd
        usuario.username = user.username
        usuario.image = user.image
        db.commit()
        return usuario
    else:
        raise Exception("Usuario no encontrado")

@router.delete("/{email}/remove")
def delete_user(email:str, db:Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.email == email).first()
    if usuario:
        db.delete(usuario)
        db.commit()
        return {"Mensaje":"Usuario borrado"}
    else:
        raise Exception("Usuario no encontrado")

