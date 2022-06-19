from fastapi import FastAPI

from database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from routers import korisnici_router,lijekovi_router,obavijesti_router,odogovorne_osobe_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://pantagane-web-app.herokuapp.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["set-cookie"],
)

app.include_router(korisnici_router.router)
app.include_router(lijekovi_router.router)
app.include_router(obavijesti_router.router)
app.include_router(odogovorne_osobe_router.router)