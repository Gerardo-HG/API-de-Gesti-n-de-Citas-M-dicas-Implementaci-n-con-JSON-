## Descripción

Esta API permite gestionar citas médicas de manera eficiente. Esta es la primera versión del proyecto, donde se utiliza archivos JSON para el almacenamiento de datos.
Incluye funcionalidades como el registro de pacientes, médicos y citas, verificando la consistencia y evitando duplicados en los DNIs entre pacientes y médicos.

La API está desarrollada con FastAPI, un framework rápido y moderno basado en Python, ideal para construir APIs robustas y escalables.


## Características principales
- Registro de pacientes y médicos con validación de DNIs.
- Registro de citas médicas asegurando la consistencia de datos.
- Uso de archivos JSON como sistema de almacenamiento.
- Validación automática de datos con Pydantic.
- Middleware de autenticación JWT.

## Requisitos
- Python 3.10 o superior
- FastAPI
- Uvicorn

## Instalación
1. Clona este repositorio
```

git clone https://github.com/tu-usuario/API-CitasMedicas-JSON.git

```

3. Navega al directorio del proyecto
```

cd API-CitasMedicas-JSON

```

4. Crea un entorno virtual e instala las dependencias
```

python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt

```

## Ejecución
1. Inicial el servidor con Uvicorn
```

uvicorn main:app --reload

```
2. Accede a la documentación interactiva de la API en :
   - Swagger UI: http://127.0.0.1:8000/docs 
   - Redoc: http://127.0.0.1:8000/redoc

## Endpoints principales

### Pacientes

- POST /pacientes: Registrar un nuevo paciente.
- GET /pacientes: Obtener todos los pacientes.

### Médicos

- POST /medicos: Registrar un nuevo médico.
- GET /medicos: Obtener todos los médicos.

### Citas Médicas

- POST /citas: Registrar una nueva cita.
- GET /citas: Obtener todas las citas.

### Estructura del Proyecto

API-CitasMedicas-JSON/
│
├── main.py               # Archivo principal para iniciar la API
│
├── routes/               # Rutas de la API
│   ├── routes_pacientes.py   # Rutas relacionadas con pacientes
│   ├── routes_medicos.py     # Rutas relacionadas con médicos
│   ├── routes_citas.py       # Rutas relacionadas con citas médicas
│
├── utils/                # Funciones auxiliares y utilidades
│   ├── jwt_manager.py        # Manejo de autenticación JWT
│   ├── validators.py         # Validación de datos compartidos (opcional)
│
├── data/                 # Archivos de almacenamiento JSON
│   ├── patients.json         # Datos de pacientes
│   ├── medics.json           # Datos de médicos
│   ├── appointments.json     # Datos de citas médicas
│
├── requirements.txt      # Dependencias del proyecto
│
├── README.md             # Documentación del proyecto
│
└── LICENSE               # Licencia del proyecto


