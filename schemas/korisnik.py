from typing import List
from pydantic import BaseModel

from schemas.obavijest_lijek import ObavijestLijekOut

class KorisnikBase(BaseModel):
    ime:str
    prezime:str
    korisnickoIme:str
    uloga:str

    class Config:
        orm_mode = True

class KorisnikIn(KorisnikBase):
    lozinka:str

class KorisnikOut(KorisnikBase):
    idKorisnik:int

class KorisnikLogin(BaseModel):
    korisnickoIme:str
    lozinka:str
    class Config:
        orm_mode=True