from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.obavijest_lijek import ObavijestLijek

from schemas.obavijest_lijek import ObavijestLijekOut

router = APIRouter(prefix="/obavijest", tags=["obavijest"])


@router.get("/",response_model=List[ObavijestLijekOut])
def list_obavijesti(db:Session = Depends(get_db)):
    obavijesti = db.query(ObavijestLijek).all()
    return obavijesti



