from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Paciente(BaseModel):
    nombre: str
    edad: int
    frecuencia_cardiaca: int
    saturacion: int
    temperatura: float
    dolor: int

def calcular_prioridad(p):
    puntos = 0

    if p.saturacion < 90:
        puntos += 5
    if p.frecuencia_cardiaca > 120:
        puntos += 4
    if p.dolor >= 8:
        puntos += 3
    if p.edad > 65:
        puntos += 2
    if p.temperatura > 39:
        puntos += 2

    if puntos >= 8:
        return "Nivel 1 - Crítico"
    elif puntos >= 6:
        return "Nivel 2 - Muy urgente"
    elif puntos >= 4:
        return "Nivel 3 - Urgente"
    elif puntos >= 2:
        return "Nivel 4 - Poco urgente"
    else:
        return "Nivel 5 - No urgente"

@app.post("/triaje")
def triaje(paciente: Paciente):
    prioridad = calcular_prioridad(paciente)
    return {"nombre": paciente.nombre, "prioridad": prioridad}
