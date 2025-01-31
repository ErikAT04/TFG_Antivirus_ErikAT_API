from fastapi import APIRouter, Depends
from app.repository import Schemas
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.database.database import get_db
from app.database import models
from app.auth import auth
from app.routers import UserRouter

router = APIRouter(prefix="/api/devices", tags=["Devices"])

@router.get("/")
def get_all_devices(db:Session = Depends(get_db), token:str = Depends(auth.oauth2_scheme)):
    devList = db.query(models.Device).all()
    return devList

@router.get("/{id}")
def get_devices_by_id(id:str, db:Session = Depends(get_db)):
    dev = db.query(models.Device).filter(models.Device.id == id).first()
    if dev:
        return dev
    else:
        raise Exception("Dispositivo no encontrado")
    
@router.get("/fromuser/{string}")
def get_all_devices_from_specified_user(string:str, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(or_(models.User.email == string, models.User.username == string)).first()
    if user:
        devList = db.query(models.Device).filter(models.Device.user == user.email).all()
        return devList
    return {"Error" : "Usuario no Encontrado"}
    
@router.post("/insert")
def insert_device(device:Schemas.Device, db:Session = Depends(get_db) ):
    dev = models.Device()
    dev.dev_name = device.dev_name
    dev.id = device.id
    dev.dev_type = device.dev_type
    dev.join_in = device.join_in
    dev.last_scan = device.last_scan
    if device.user:
        dev.user = device.user
    db.add(dev)
    db.commit()
    return dev

@router.put("/{id}/update")
def update_device(id:str, device:Schemas.Device, db:Session = Depends(get_db), token:str = Depends(auth.oauth2_scheme)):
    dev = db.query(models.Device).filter(models.Device.id == id).first()
    if dev:
        dev.dev_name = device.dev_name
        dev.id = device.id
        dev.dev_type = device.dev_type
        dev.join_in = device.join_in
        dev.last_scan = device.last_scan
        dev.user = device.user
        db.commit()
        return dev
    else:
        raise Exception("Dispositivo no encontrado")
    
@router.delete("/{id}/remove")
def delete_device(id:str, db:Session = Depends(get_db), token:str = Depends(auth.oauth2_scheme)):
    dev = db.query(models.Device).filter(models.Device.id == id).first()
    if dev:
        db.delete(dev)
        db.commit()
        return "Eliminado correctamente"
    else:
        raise Exception("Dispositivo no encontrado")
    