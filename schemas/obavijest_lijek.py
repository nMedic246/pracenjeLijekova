from pydantic import BaseModel

from schemas.lijek import LijekOut


class ObavijestLijekBase(BaseModel):
    idKorisnik:int
    idLijek:int
    vrijemeObavijesti:str
    kolicina:str
    uzetLijek: bool

    class Config:
        orm_mode = True

class ObavijestLijekOut(ObavijestLijekBase):
    lijek: LijekOut
    