from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Lijek(Base):

    __tablename__ = "Lijek"
    
    idLijek = Column(Integer,primary_key = True, index = True)
    naziv = Column(String)
    pocetniDatum = Column(String)
    trajanjeTerapije  = Column(Integer)
    daniUzimanja = Column(String)

    obavijesti = relationship("ObavijestLijek",back_populates="lijek",cascade="all,delete")
    pacijentLijekovi = relationship("PacijentLijek",back_populates="lijek",cascade="all,delete")