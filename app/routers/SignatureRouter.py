from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.models import Signature
from app.database.database import get_db

router = APIRouter(prefix="/api/signatures", tags=["Signatures"])

@router.get("/")
def get_all_signatures(db:Session = Depends(get_db)):
    return db.query(Signature).all()