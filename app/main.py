from fastapi import FastAPI, Depends, APIRouter

# from app.v1.database.db import get_db
from app.v1.router import usuario


app = FastAPI()


@app.get("/")
def bienvenida():
    integrantes = ["Carlos Torres A", "Jose Figuera", "Rafael Perez"]
    return {
        "mensaje": "Bienvenido al proyecto Final FastApi",
        "integrantes": integrantes,
    }


app.include_router(usuario.router)
