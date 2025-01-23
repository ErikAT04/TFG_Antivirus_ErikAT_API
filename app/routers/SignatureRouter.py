from fastapi import APIRouter
from app.repository.Schemas import Signature

router = APIRouter(prefix="/api/signatures")

@router.get("/")
def get_all_signatures():
    sigList = []
    with open("app/files/virusDef.txt", "r") as file:
        for line in file.readlines():
            auxList = line.split("|")
            sigList.append(Signature(signature=auxList[1], extendedType=auxList[2], type=auxList[3]))
    return sigList