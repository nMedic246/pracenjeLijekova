import re
from turtle import back
from xmlrpc.client import Boolean
from sqlalchemy import Column, ForeignKey, Integer, String,Boolean
from sqlalchemy.orm import relationship
from database import Base

class OdgovornaOsoba(Base):

    __tablename__ = "OdgovornaOsoba"

    idOdgovornaOsoba = Column(Integer, ForeignKey("Korisnik.idKorisnik"),primary_key=True)
    idBolesnik = Column(Integer, ForeignKey("Korisnik.idKorisnik"),primary_key=True)
    vrijemeObavijestiUMinutama = Column(Integer,primary_key= True)

    korisnik = relationship("Korisnik", back_populates ="bolesnici",foreign_keys=[idBolesnik])
    odgovornaOsoba = relationship("Korisnik",back_populates="odgOsoba",foreign_keys=[idOdgovornaOsoba])