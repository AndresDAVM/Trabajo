from sqlalchemy import Column, Integer, String, Float
from database import Base

class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    edad = Column(Integer)
    frecuencia_cardiaca = Column(Integer)
    saturacion = Column(Integer)
    temperatura = Column(Float)
    dolor = Column(Integer)
    prioridad = Column(String)
