from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.lijek import Lijek
from sqlalchemy.exc import IntegrityError, NoResultFound

from schemas.lijek import  LijekBase, LijekOut, LijekUpdate

router = APIRouter(prefix="/lijek", tags=["lijek"])


@router.get("/sviLijekovi",response_model=List[LijekOut])
def list_lijekovi(db:Session = Depends(get_db)):
    lijekovi = db.query(Lijek).all()
    for lijek in lijekovi:
        lijek.daniUzimanja = lijek.daniUzimanja.split(";")
    return lijekovi

@router.get("/{id_lijek}",response_model=LijekOut)
def get_lijek_byId(id_lijek:str,db:Session = Depends(get_db)):

    try:
        lijek_db =  db.query(Lijek).filter(Lijek.idLijek == id_lijek).one()
        lijek_db.daniUzimanja = lijek_db.daniUzimanja.split(";")
        return lijek_db
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Lijek does not exist."
        )

@router.post("/noviLijek",response_model=LijekOut)
def create_lijek(lijek : LijekBase, db:Session = Depends(get_db)):

    try:
        lijek_db = Lijek(**lijek.dict())
        db.add(lijek_db)
        db.commit()
        lijek_db.daniUzimanja = lijek_db.daniUzimanja.split(";")

        return lijek_db   

    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Lijek already exists."
        )

@router.delete("/{id_lijek}")
def delete_lijek(id_lijek: str, db: Session = Depends(get_db)):
    try:

        db.query(Lijek).filter(Lijek.idLijek == id_lijek).one()
        db.query(Lijek).filter(Lijek.idLijek == id_lijek).delete()
        db.commit()
        
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lijek with id: {id_lijek} not found.",
        )    

@router.put("/{id_lijek}", response_model=LijekOut)
def update_lijek(id_lijek: str,lijek: LijekUpdate,db: Session = Depends(get_db)):
   
    try:
        
        lijek_query = db.query(Lijek).filter(Lijek.idLijek == id_lijek)
        lijek_query.one()
        update_dict = lijek.dict(exclude_none=True, exclude_unset=True)
        lijek_query.update(update_dict)
        lijek_model = lijek_query.one()
        db.commit()
        lijek_model.daniUzimanja = lijek_model.daniUzimanja.split(";")
        return lijek_model

    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lijek with id: {id_lijek} not found.",
        )