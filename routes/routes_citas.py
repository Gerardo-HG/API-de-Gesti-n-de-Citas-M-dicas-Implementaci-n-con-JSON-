from fastapi import APIRouter, Path, Body, HTTPException, Depends
from fastapi.responses import JSONResponse
from schemas.citas_medicas import CitaMedica
from uuid import UUID
from middlewares.jwt_bearer import JWTBearer
import json
from utils.data_loader import load_dnis

cita_router = APIRouter()

# Funciones auxiliares para manejar archivos
def load_appointments():
    try:
        with open("citas_medicas.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="El archivo 'citas_medicas.json' no existe.")
    except json.JSONDecodeError:
        return []

def save_appointments(appointments):
    with open("citas_medicas.json", "w") as file:
        json.dump(appointments, file, indent=4)

## Mostrar todas las citas
@cita_router.get(
    path="/citas",
    tags=["Cita Medica"],
    status_code=200,
    dependencies=[Depends(JWTBearer())]
)
def show_appointments():
    appointments = load_appointments()
    return JSONResponse(status_code=200, content=appointments)

## Registrar una nueva cita
@cita_router.post(
    path="/citas",
    tags=['Cita Medica'],
    status_code=201,
    dependencies=[Depends(JWTBearer())]
)
def create_appointment(appointment: CitaMedica = Body(...)):
    
    pacientes_dnis = load_dnis("patients.json", "dni")
    medicos_dnis = load_dnis("medics.json", "dni")
    

    if appointment.paciente_dni not in pacientes_dnis or not appointment.paciente_dni.isnumeric():
        raise HTTPException(status_code=400, detail="DNI del paciente no válido.")
    
    if appointment.medico_dni not in medicos_dnis or not appointment.medico_dni.isnumeric():
        raise HTTPException(status_code=400, detail="DNI del médico no válido.")
    
    appointments = load_appointments()

    appointment.id = str(appointment.id)
    appointment.fecha = str(appointment.fecha)

    appointments.append(appointment.dict())
    save_appointments(appointments)
    return JSONResponse(status_code=201, content={"message": "Cita médica registrada con éxito"})

## Obtener una cita por ID
@cita_router.get(
    path="/citas/{id}",
    tags=['Cita Medica'],
    response_model=CitaMedica,
    status_code=200
)
def get_appointment(id: UUID = Path(..., description="ID único de la cita médica")):
    appointments = load_appointments()
    for appointment in appointments:
        if appointment['id'] == str(id):
            return JSONResponse(status_code=200, content=appointment)
    raise HTTPException(status_code=404, detail="Cita médica no encontrada.")

## Actualizar una cita
@cita_router.put(
    path="/citas/{id}",
    tags=['Cita Medica'],
    status_code=200
)
def update_appointment(
    id: UUID = Path(..., description="ID único de la cita médica a actualizar"),
    appointment_u: CitaMedica = Body(...)
):
    appointments = load_appointments()
    for appointment in appointments:
        if appointment['id'] == str(id):
            appointment.update(appointment_u.dict())
            save_appointments(appointments)
            return JSONResponse(status_code=200, content={"message": "Cita médica actualizada con éxito"})
    raise HTTPException(status_code=404, detail="Cita médica no encontrada.")

## Eliminar una cita
@cita_router.delete(
    path="/citas/{id}",
    tags=['Cita Medica'],
    status_code=200
)
def delete_appointment(id: UUID = Path(..., description="ID único de la cita médica a eliminar")):
    appointments = load_appointments()
    updated_appointments = [appointment for appointment in appointments if appointment['id'] != str(id)]
    if len(appointments) == len(updated_appointments):
        raise HTTPException(status_code=404, detail="Cita médica no encontrada.")
    save_appointments(updated_appointments)
    return JSONResponse(status_code=200, content={"message": "Cita médica eliminada con éxito"})
