from fastapi import APIRouter, Path, Body, HTTPException
from schemas.patient import Paciente
import json
from fastapi.responses import JSONResponse
from typing import Optional, List

patient_router = APIRouter()

# Path Operations

## Pacientes

## Mostrar Pacientes
@patient_router.get(
    path="/pacientes",
    tags=['Paciente'],
    response_model=List[Paciente],
    status_code=200
)
def show_patients() -> List[Paciente]:
    try:
        with open("patients.json", "r") as file:
            patients = json.load(file)
            return JSONResponse(status_code=200, content=patients)
    except FileNotFoundError:
        return {"error" : "El archivo 'patients.json' no existe."}

## Registrar Paciente
@patient_router.post(
    path="/pacientes",
    tags=['Paciente'],
    status_code=201    
)
def create_patient(patient : Paciente):
    try:
        with open("patients.json",'r+') as file:
            try:
                patients = json.load(file)
            except json.JSONDecodeError:
                patients = []
            
            patient_dict = patient.dict()
            if patient_dict["fecha_nacimiento"]:
                patient_dict["fecha_nacimiento"] = patient_dict["fecha_nacimiento"].isoformat()

            patients.append(patient_dict)
            file.seek(0)
            file.truncate()

            json.dump(patients, file, indent=4)

        return JSONResponse(status_code=200, content={"message": "Se ha registrado el paciente"})

    except FileNotFoundError:
        return {"message": "El archivo 'patients.json' no existe."}
    
    except Exception as e:
        return {"error" : " Ha ocurrido un error : "+str(e)}
    
## Obtener Paciente
@patient_router.get(
    path="/pacientes/{dni}",
    tags=['Paciente'],
    response_model=Paciente
)
def get_patient(dni: str =Path(description="DNI of a patient")) -> Paciente:
    try:
        with open("patients.json", "r") as file:
            patients = json.load(file)
            for patient in patients:
                if patient['dni'] == dni:
                    return JSONResponse(status_code=200, content=patient)
            raise HTTPException(status_code=404, detail="Paciente no encontrado")
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="El archivo 'patients.json' no existe.")
    
## Eliminar Paciente
@patient_router.delete(
    path="/pacientes/{dni}",
    tags=['Paciente'],
    status_code=200
)
def delete_patient(dni: str = Path(description="DNI of a patient")):
    try:
        with open("patients.json", "r") as file:
            patients = json.load(file)
            
            patient_found = None
            for patient in patients:
                if patient['dni'] == dni:
                    patient_found = patient 
                    break

        if not patient_found:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")

        patients = [patient for patient in patients if patient['dni'] != dni]

        with open("patients.json", 'w') as file:
            json.dump(patients, file, indent=4)

            return JSONResponse(status_code=200, content={"message" : " Paciente eliminado con éxito"})

    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="El archivo 'patients.json' no existe.")
    
## Actualizar Paciente
@patient_router.put(
    path="/pacientes/{dni}",
    tags=['Paciente'],
    status_code=200
    )
def update_patient(dni: str = Path(description="DNI of a patient"), patient_u: Paciente = Body(...)):
    try:
        with open("patients.json", "r") as file:
            patients = json.load(file)
            
            patient_found = None
            for patient in patients:
                if patient['dni'] == dni:
                    patient_found = patient
                    break
            
            patient_found['nombre'] = patient_u.nombre
            patient_found['apellido'] = patient_u.apellido
            patient_found['email'] = patient_u.email
            patient_found['fecha_nacimiento'] = str(patient_u.fecha_nacimiento)

        with open("patients.json", "w") as file:
            json.dump(patients, file, indent=4)
            return JSONResponse(status_code=200, content={"message" : " Paciente actualizado con éxito"})


        if not patient_found:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")

        with open("patients.json", 'w') as file:
            json.dump(patients, file, indent=4)

            return JSONResponse(status_code=200, content={"message" : " Paciente actualizado con éxito"})

    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="El archivo 'patients.json' no existe.")
    