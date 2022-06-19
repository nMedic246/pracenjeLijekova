from typing import List
from fastapi import APIRouter, Depends,HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.korisnik import Korisnik
from models.obavijest_lijek import ObavijestLijek
from models.odgovorna_osoba import OdgovornaOsoba
from schemas.korisnik import KorisnikOut
from schemas.obavijest_lijek import ObavijestLijekOut
from schemas.odgovorna_odoba import OdgovornaOsobaBase
from sqlalchemy.exc import NoResultFound


router = APIRouter(prefix="/odgovornaOsoba", tags=["odgovornaOsoba"])

@router.get("/obavijestiPacijenata/{id_odg_osoba}",response_model = List[ObavijestLijekOut])
def get_obavijesti_pacijenata(id_odg_osoba:str, db :Session = Depends(get_db)):

    obavijesti = db.query(ObavijestLijek).join(Korisnik,Korisnik.idKorisnik == ObavijestLijek.idKorisnik 
                ).join(OdgovornaOsoba,OdgovornaOsoba.idBolesnik==Korisnik.idKorisnik
                ).filter(OdgovornaOsoba.idOdgovornaOsoba==id_odg_osoba).all()

    lijekovi = set()
    for o in obavijesti:
        if(o.lijek.idLijek not in lijekovi):
            lijekovi.add(o.lijek.idLijek)
            o.lijek.daniUzimanja = o.lijek.daniUzimanja.split(";")
          
    return obavijesti

@router.post("/dodajPacijenta",response_model = KorisnikOut)
def dodaj_novog_pacijenta(odg_osoba : OdgovornaOsobaBase, db :Session = Depends(get_db)):

    try:
        db.query(Korisnik).filter(Korisnik.idKorisnik==odg_osoba.idOdgovornaOsoba).one()
        pacijent = db.query(Korisnik).filter(Korisnik.idKorisnik==odg_osoba.idBolesnik).one()

        odg_osoba_db = OdgovornaOsoba(**odg_osoba.dict())
        db.add(odg_osoba_db)
        db.commit()
        return pacijent
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Odgovorna osoba or pacijent with the given id does not exist."
        )
