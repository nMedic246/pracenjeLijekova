from pydantic import BaseModel
from schemas.lijek import LijekOut

class PacijentLijekBase(BaseModel):
    idLijek:int
    idPacijent:int

    class Config:
        orm_mode = True

class PacijentLijekOut(BaseModel):
    lijek: LijekOut
    class Config:
        orm_mode = True