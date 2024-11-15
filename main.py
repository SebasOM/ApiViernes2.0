from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.modelosApp import Usuario, Base
from app.api.routes.rutas import rutas

from starlette.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware


#Activar el ORM
Base.metadata.create_all(bind = engine)


#Variable para administrar la aplicacion
app = FastAPI()

#Activando el cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"] 
)

#Activo el API
@app.get('/')
def main():
    return RedirectResponse(url = '/docs')

app.include_router(rutas)