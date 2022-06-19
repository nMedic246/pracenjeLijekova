from lib2to3.pytree import Base
from pydantic import BaseModel

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

class KorisnikNoviLijek(BaseModel):
    korisnickoIme:str
    nazivLijek:str

    class Cofig:
        orm_mode = True