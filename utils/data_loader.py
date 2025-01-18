import json

def load_dnis(filename: str, key: str, existing_dnis: set = None) -> set:
    """
    Carga un conjunto de DNIs únicos desde un archivo JSON y verifica que no haya DNIs duplicados.

    Args:
        filename (str): Ruta del archivo JSON.
        key (str): Clave en el archivo JSON donde se almacenan los DNIs.
        existing_dnis (set, optional): Conjunto de DNIs ya existentes para evitar duplicados. Default es None.

    Returns:
        set: Conjunto de DNIs únicos.

    Raises:
        ValueError: Si se encuentra un DNI duplicado en el archivo o si un DNI de paciente es el mismo que un médico.
    """
    if existing_dnis is None:
        existing_dnis = set()

    with open(filename, 'r') as file:
        data = json.load(file)

    dnis = set()
    for item in data:
        if key in item:
            dni = item[key]
            if dni in existing_dnis:
                raise ValueError(f"DNI '{dni}' encontrado en otra clase")
            
            if dni in dnis:
                raise ValueError(f"DNI duplicado encontrado: {dni}")
            
            dnis.add(dni)

    return dnis