from fastapi import APIRouter, Path, Body, HTTPException
from schemas.patient import Paciente
import json
from fastapi.responses import JSONResponse
from schemas.medic import Medico

medic_router = APIRouter()

# Medicos

## Motrar Medicos
@medic_router.get(
        path="/medicos",
        tags=["Medico"],
        status_code=200
)
def show_medics():
    try:
        with open("medics.json", "r") as file:
            medics = json.load(file)
            return JSONResponse(status_code=200, content=medics)
    except FileNotFoundError:
        return {"error" : "El archivo 'medics.json' no existe."}
    
## Registrar Medico
@medic_router.post(
    path="/medicos",
    tags=['Medico'],
    status_code=201    
)
def create_medic(medic : Medico):
    try:
        with open("medics.json",'r+') as file:
            try:
                medics = json.load(file)
            except json.JSONDecodeError:
                medics = []
            
            medic_dict = medic.dict()

            medics.append(medic_dict)
            file.seek(0)
            file.truncate()

            json.dump(medics, file, indent=4)

        return JSONResponse(status_code=200, content={"message": "Se ha registrado el medico"})

    except FileNotFoundError:
        return {"message": "El archivo 'medicos.json' no existe."}
    
    except Exception as e:
        return {"error" : " Ha ocurrido un error : "+str(e)}
    
## Obtener Medico
@medic_router.get(
    path="/medicos/{dni}",
    tags=['Medico'],
    response_model=Medico
)
def get_medic(dni: str =Path(description="DNI of a medic")) -> Medico:
    try:
        with open("medics.json", "r") as file:
            medics = json.load(file)
            for medic in medics:
                if medic['dni'] == dni:
                    return JSONResponse(status_code=200, content=medic)
            raise HTTPException(status_code=404, detail="Medico no encontrado")
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="El archivo 'medics.json' no existe.")
    
## Eliminar Medico
@medic_router.delete(
    path="/medicos/{dni}",
    tags=['Medico'],
    status_code=200
)
def delete_medic(dni: str = Path(description="DNI of a medic")):
    try:
        with open("medics.json", "r") as file:
            medics = json.load(file)
            
            medic_found = None
            for medic in medics:
                if medic['dni'] == dni:
                    medic_found = medic 
                    break

        if not medic_found:
            raise HTTPException(status_code=404, detail="Medico no encontrado")

        medics = [medic for medic in medics if medic['dni'] != dni]

        with open("medics.json", 'w') as file:
            json.dump(medics, file, indent=4)

            return JSONResponse(status_code=200, content={"message" : "Medico eliminado con éxito"})

    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="El archivo 'medics.json' no existe.")
    
## Actualizar Medico
@medic_router.put(
    path="/medicos/{dni}",
    tags=['Medico'],
    status_code=200
    )
def update_medic(dni: str = Path(description="DNI of a medic"), medic_u: Medico = Body(...)):
    try:
        with open("medics.json", "r") as file:
            medics = json.load(file)
            
            medic_found = None
            for medic in medics:
                if medic['dni'] == dni:
                    medic_found = medic
                    break
            
            medic_found['nombre'] = medic_u.nombre
            medic_found['apellido'] = medic_u.apellido
            medic_found['email'] = medic_u.email
            medic_found['anios_experiencia'] = medic_u.anios_experiencia
            medic_found['especialidad'] = medic_u.especialidad

        with open("medics.json", "w") as file:
            json.dump(medics, file, indent=4)
            return JSONResponse(status_code=200, content={"message" : " Medico actualizado con éxito"})


        if not medic_found:
            raise HTTPException(status_code=404, detail="Medico no encontrado")

        with open("medics.json", 'w') as file:
            json.dump(medics, file, indent=4)

            return JSONResponse(status_code=200, content={"message" : " Medico actualizado con éxito"})

    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="El archivo 'medics.json' no existe.")
    