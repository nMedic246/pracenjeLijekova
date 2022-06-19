from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from database import Base

class PacijentLijek(Base):

    __tablename__ = "PacijentLijek"
    
    idLijek = Column(Integer, ForeignKey("Lijek.idLijek",ondelete='CASCADE'),primary_key=True)
    idPacijent = Column(Integer,ForeignKey("Korisnik.idKorisnik",ondelete='CASCADE'),primary_key=True)

    lijek = relationship("Lijek", back_populates ="pacijentLijekovi")
    pacijent = relationship("Korisnik",back_populates = "pacijentLijekovi")