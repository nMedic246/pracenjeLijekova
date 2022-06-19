from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.korisnik import Korisnik

from passlib.context import CryptContext
from sqlalchemy.exc import NoResultFound

from sqlalchemy.exc import IntegrityError
from models.pacijent_lijek import PacijentLijek
from schemas.korisnik import KorisnikIn, KorisnikLogin, KorisnikOut
from schemas.pacijent_lijek import PacijentLijekOut

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(prefix="/korisnik", tags=["korisnik"])

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


@router.post("/login",response_model= KorisnikOut,response_model_exclude_unset=True)
def user_login(korisnik:KorisnikLogin,db: Session= Depends(get_db)):
    """User login.

    Args:
        User username and password.

    Raises:
        HTTPException: 401 if the credentials are wrong.

    Returns:
        (KorisnikOut)
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Pogrešno korisničko ime ili lozinka"
    )

    korisnik_db = db.query(Korisnik).filter(Korisnik.korisnickoIme == korisnik.korisnickoIme).first()
    if korisnik_db is None:
        raise credentials_exception

    if not verify_password(korisnik.lozinka, korisnik_db.lozinka):
        raise credentials_exception
    return korisnik_db
    
   

@router.post("/noviKorisnik", response_model=KorisnikOut)
def create_user(korisnik: KorisnikIn, db: Session = Depends(get_db)):
    """Creates a user.

    Args:
        user (KorisnikIn): api payload for creating a user.

    Raises:
        HTTPException: 409 if the user already exists.

    Returns:
        (UserOut)
    """

    try:
        print(korisnik)
        user_db = Korisnik(**korisnik.dict())
        user_db.lozinka = pwd_context.hash(user_db.lozinka)
        db.add(user_db)
        db.commit()
        return user_db
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Korisnik already exists."
        )

@router.get("/korisnikLijekovi/{id_korisnik}", response_model= List[PacijentLijekOut])
def get_korisnik_lijekovi(id_korisnik:int, db:Session = Depends(get_db)):
    try:
        lijekovi = db.query(PacijentLijek).filter(PacijentLijek.idPacijent == id_korisnik).all()
        for pl in lijekovi:
            pl.lijek.daniUzimanja = pl.lijek.daniUzimanja.split(";")
        return lijekovi

    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Korisnik with the given id does not exist."
        )

@router.get("/korisnikLijekovi/{id_korisnik}", response_model= List[PacijentLijekOut])
def get_korisnik_lijekovi(id_korisnik:int, db:Session = Depends(get_db)):
    try:
        lijekovi = db.query(PacijentLijek).filter(PacijentLijek.idPacijent == id_korisnik).all()
        
        print(lijekovi)
        return lijekovi

    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Korisnik with the given id does not exist."
        )

