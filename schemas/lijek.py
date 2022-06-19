from lib2to3.pgen2.token import OP
from typing import List, Optional
from pydantic import BaseModel

from database import Base


class LijekBase(BaseModel):
    naziv:str
    pocetniDatum:str
    trajanjeTerapije:int
    daniUzimanja:str

    class Config:
        orm_mode = True

class LijekOut(BaseModel):
    idLijek:int
    pocetniDatum:str
    trajanjeTerapije:int
    daniUzimanja:List[str]
    class Config:
        orm_mode = True

class LijekUpdate(BaseModel):
    naziv : Optional[str]
    pocetniDatum : Optional[str]
    trajanjeTerapije : Optional[int]
    daniUzimanja: Optional[str]