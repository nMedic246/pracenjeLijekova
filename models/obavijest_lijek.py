from sqlalchemy import Column, ForeignKey, Integer, String,Boolean
from sqlalchemy.orm import relationship
from database import Base

class ObavijestLijek(Base):

    __tablename__ = "ObavijestLijek"

    idObavijest = Column(Integer, primary_key=True, index=True)
    idKorisnik = Column(Integer, ForeignKey("Korisnik.idKorisnik",ondelete='CASCADE'))
    idLijek = Column(Integer, ForeignKey("Lijek.idLijek",ondelete='CASCADE'))
    vrijemeObavijesti = Column(String)
    datumObavijesti = Column(String)
    kolicina = Column(String)
    uzetLijek = Column(Boolean)

    korisnik = relationship("Korisnik", back_populates ="obavijesti")
    lijek = relationship("Lijek",back_populates = "obavijesti")