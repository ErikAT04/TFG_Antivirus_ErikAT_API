from pydantic import BaseModel
class Signature(BaseModel):
    signature:str
    type:str
    extendedType:str