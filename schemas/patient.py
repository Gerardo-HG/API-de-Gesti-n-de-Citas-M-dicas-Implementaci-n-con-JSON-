#Python
from typing import Optional
from datetime import date, datetime

#Pydantic
from pydantic import BaseModel, Field
from pydantic import EmailStr


class Paciente(BaseModel):
    nombre : str = Field(..., min_length=3, max_length=10)
    apellido : str = Field(..., min_length=4, max_length=10)
    dni : str = Field(...)
    fecha_nacimiento : Optional[date] = Field(default=datetime.now())
    email : EmailStr = Field(...)

    class Config:
        json_schema_extra = {
            "example" : {
                "nombre" : "Gerardo",
                "apellido" : "Herrera",
                "dni" : "1234567",
                "fecha_nacimiento" : "2024-09-24",
                "email" : "gerardo123@gmail.com"
            }
        }