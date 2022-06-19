from collections import UserList
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from models.odgovorna_osoba import OdgovornaOsoba

class Korisnik(Base):

    __tablename__ = "Korisnik"

    idKorisnik = Column(Integer, primary_key=True, index=True)
    ime = Column(String)
    prezime = Column(String)
    korisnickoIme = Column(String,unique=True)
    lozinka = Column(String)
    uloga = Column(String)

    obavijesti = relationship("ObavijestLijek",back_populates="korisnik")
    pacijentLijekovi = relationship("PacijentLijek",back_populates="pacijent")
    bolesnici = relationship("OdgovornaOsoba",back_populates="korisnik",foreign_keys=[OdgovornaOsoba.idBolesnik])
    odgOsoba = relationship("OdgovornaOsoba",back_populates="odgovornaOsoba",uselist = False,foreign_keys=[OdgovornaOsoba.idOdgovornaOsoba])