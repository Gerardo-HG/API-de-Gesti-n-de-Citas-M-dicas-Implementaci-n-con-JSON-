#Python
from typing import Optional
from datetime import date, datetime

#Pydantic
from pydantic import BaseModel, Field
from pydantic import EmailStr

class Medico(BaseModel):
    
    dni : str = Field(...)
    nombre: str = Field (min_length=3, max_length=10)
    apellido: str = Field(min_length=4, max_length=10)
    especialidad: Optional[str] = Field(default="Medicina General")
    anios_experiencia : int  = Field(ge=0)
    email: EmailStr = Field(...)

    class Config:
        json_schema_extra = {
            "example" : {
                "dni": "9876543",
                "nombre" : "Pepe",
                "apellido" : "Suarez",
                "especialidad": "Cardiologo",
                "anios_experiencia":2, 
                "email" : "pepelucho123@gmail.com"
            }
        }