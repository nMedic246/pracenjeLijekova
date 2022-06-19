from typing import List
from pydantic import BaseModel

from schemas.lijek import LijekOut
from schemas.obavijest_lijek import ObavijestLijekOut

class PacijentLijekBase(BaseModel):
    idLijek:int
    idPacijent:int

    class Config:
        orm_mode = True

class PacijentLijekOut(BaseModel):
    lijek: LijekOut
    class Config:
        orm_mode = True