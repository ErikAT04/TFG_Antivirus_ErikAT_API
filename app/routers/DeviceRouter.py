from fastapi import APIRouter, Depends
from app.repository import Schemas
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database import models

router = APIRouter(prefix="/api/devices")

@router.get("/")
def get_all_devices(db:Session = Depends(get_db)):
    devList = db.query(models.Device).all()
    return devList

@router.get("/{id}")
def get_devices_by_id(id:str, db:Session = Depends(get_db)):
    dev = db.query(models.Device).filter(models.Device.id == id).first()
    if dev:
        return dev
    else:
        raise Exception("Dispositivo no encontrado")
    
@router.post("/insert")
def insert_device(device:Schemas.Device, db:Session = Depends(get_db)):
    dev = models.Device()
    dev.dev_name = device.dev_name
    dev.id = device.id
    dev.dev_type = device.dev_type
    dev.join_in = device.join_in
    dev.last_scan = device.last_scan
    dev.user = device.user
    db.add(dev)
    db.commit()
    return dev

@router.put("/{id}/update")
def update_device(id:str, device:Schemas.Device, db:Session = Depends(get_db)):
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
    
@router.put("/{id}/remove")
def delete_device(id:str, db:Session = Depends(get_db)):
    dev = db.query(models.Device).filter(models.Device.id == id).first()
    if dev:
        db.delete(dev)
        db.commit()
        return "Eliminado correctamente"
    else:
        raise Exception("Dispositivo no encontrado")