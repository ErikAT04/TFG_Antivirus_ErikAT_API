from fastapi import APIRouter
from models.Signature import Signature

router = APIRouter(prefix="/api/signatures")

@router.get("/")
def getAllSigs():
    sigList = []
    with open("files/virusDef.txt", "r") as file:
        for line in file.readlines():
            auxList = line.split("|")
            sigList.append(Signature(signature=auxList[1], extendedType=auxList[2], type=auxList[3]))
    return sigList