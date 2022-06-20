from typing import List
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
from models.korisnik import Korisnik
from models.lijek import Lijek
from models.obavijest_lijek import ObavijestLijek
from models.odgovorna_osoba import OdgovornaOsoba
from sqlalchemy.exc import IntegrityError, NoResultFound
from models.pacijent_lijek import PacijentLijek


from schemas.obavijest_lijek import ObavijestLijekBase, ObavijestLijekOut, ObavijestUpdate

router = APIRouter(prefix="/obavijest", tags=["obavijest"])


@router.get("/{id_korisnik}",response_model=List[ObavijestLijekOut])
def get_moje_obavijesti(id_korisnik:str, db:Session = Depends(get_db)):
    try:
        obavijesti = db.query(ObavijestLijek).filter(ObavijestLijek.idKorisnik==id_korisnik).all()

        lijekovi = set()
        for o in obavijesti:
            if(o.lijek.idLijek not in lijekovi):
                lijekovi.add(o.lijek.idLijek)
                o.lijek.daniUzimanja = o.lijek.daniUzimanja.split(";")
        return obavijesti
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pacijent does not exist."
        )

@router.post("/dodajObavijest",response_model=ObavijestLijekOut)
def dodaj_novu_obavijest(obavijest:ObavijestLijekBase, db:Session = Depends(get_db)):
    try:
        db.query(Korisnik).filter(Korisnik.idKorisnik == obavijest.idKorisnik).one()
        db.query(Lijek).filter(Lijek.idLijek == obavijest.idLijek).one()

        noviLijek = {}
        noviLijek['idLijek'] = obavijest.idLijek
        noviLijek['idPacijent'] = obavijest.idKorisnik
        noviLijek_db = PacijentLijek(**noviLijek)
        db.add(noviLijek_db)
        
        obavijest_db = ObavijestLijek(**obavijest.dict())
        db.add(obavijest_db)
        db.commit()
        obavijest_db.lijek.daniUzimanja = obavijest_db.lijek.daniUzimanja.split(";")

        return obavijest_db   

    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Obavijest already exists."
        )
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pacijent or lijek does not exist."
        )

@router.put("/urediObavijest/{id_obavijest}",response_model=ObavijestLijekOut)
def uredi_obavijest(id_obavijest:str,obavijest_update:ObavijestUpdate, db:Session = Depends(get_db)):
    try:
        obavijest_query = db.query(ObavijestLijek).filter(ObavijestLijek.idObavijest == id_obavijest)
        obavijest_query.one()
        update_dict = obavijest_update.dict(exclude_none=True,exclude_unset=True)
        obavijest_query.update(update_dict)
        obavijest_db = obavijest_query.one()
        db.commit()
        obavijest_db.lijek.daniUzimanja = obavijest_db.lijek.daniUzimanja.split(";")

        return obavijest_db   
        
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Obavijest with the given id does not exist."
        )

@router.delete("/{id_obavijest}")
def delete_obavijest(id_obavijest: str, db: Session = Depends(get_db)):
    try:

        db.query(ObavijestLijek).filter(ObavijestLijek.idObavijest == id_obavijest).one()
        db.query(ObavijestLijek).filter(ObavijestLijek.idObavijest == id_obavijest).delete()
        db.commit()
        
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lijek with id: {id_obavijest} not found.",
        ) 

