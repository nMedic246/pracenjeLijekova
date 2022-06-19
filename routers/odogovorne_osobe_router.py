from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.korisnik import Korisnik
from models.obavijest_lijek import ObavijestLijek
from models.odgovorna_osoba import OdgovornaOsoba
from schemas.obavijest_lijek import ObavijestLijekOut


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


   