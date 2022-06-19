from typing import Optional
from pydantic import BaseModel

from schemas.lijek import LijekOut


class ObavijestLijekBase(BaseModel):
    idKorisnik:int
    idLijek:int
    vrijemeObavijesti:str
    datumObavijesti:str
    kolicina:str
    uzetLijek: bool

    class Config:
        orm_mode = True

class ObavijestLijekOut(ObavijestLijekBase):
    idObavijest:int
    lijek: LijekOut
    
class ObavijestUpdate(BaseModel):
    vrijemeObavijesti : Optional[str]
    datumObavijesti: Optional[str]
    kolicina: Optional[str]
    uzetLijek: Optional[bool]