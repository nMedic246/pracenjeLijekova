from pydantic import BaseModel

class OdgovornaOsobaBase(BaseModel):
    idOdgovornaOsoba:int
    idBolesnik:int
    vrijemeObavijestiUMinutama:int

    class Config:
        orm_mode = True