#Python
from typing import Optional
from datetime import date,datetime
from uuid import UUID

#Pydantic
from pydantic import BaseModel, Field
from pydantic import EmailStr

class CitaMedica(BaseModel):
    id : UUID = Field(
        ...
    )
    paciente_dni : str = Field(...)
    medico_dni : str = Field(...)
    fecha: date = Field(default=datetime.now().date())
    motivo : str = Field(..., min_length=5,max_length=20)
    estado : Optional[str] = Field(default="pendiente")
