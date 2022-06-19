from typing import List, Optional
from pydantic import BaseModel


class LijekBase(BaseModel):
    naziv:str
    pocetniDatum:str
    trajanjeTerapije:int
    daniUzimanja:str

    class Config:
        orm_mode = True

class LijekOut(BaseModel):
    idLijek:int
    naziv:str
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