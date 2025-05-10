from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.models import Hash
from app.database.database import get_db

router = APIRouter(prefix="/api/hashes", tags=["hashes"])

@router.get("/")
def get_all_hashes(db:Session = Depends(get_db)):
    return db.query(Hash).all()