#Python
import json

#FastAPI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi import Path, Query, Body, HTTPException

# From Schemas directory
from schemas.patient import Paciente
from schemas.medic import Medico

# From Routes directory
from routes.route_patient import patient_router
from routes.route_medic import medic_router
from routes.routes_citas import cita_router
from routes.route_user import user_router

# From Middleware directory
from middlewares.error_handler import ErrorHandler


app = FastAPI()
app.title = "API de Citas Medicas"

app.add_middleware(ErrorHandler)

app.include_router(user_router)
app.include_router(patient_router)
app.include_router(medic_router)
app.include_router(cita_router)

# Routes    
@app.get(
    path="/",
    tags=['home'],
)
def home():
    return HTMLResponse('<h1>Hello World!</h1>')

