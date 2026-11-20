# crear_base_entidades.py
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from configuracion import Base, engine

class Clinica(Base):
    __tablename__ = "clinicas"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    medico_responsable = Column(String, nullable=False)
    consultorios = relationship("Consultorio", back_populates="clinica")

class Consultorio(Base):
    __tablename__ = "consultorios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)
    clinica_id = Column(Integer, ForeignKey("clinicas.id"), nullable=False)
    clinica = relationship("Clinica", back_populates="consultorios")
    veterinarios = relationship("Veterinario", back_populates="consultorio")

class Veterinario(Base):
    __tablename__ = "veterinarios"
    id = Column(Integer, primary_key=True)
    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    email = Column(String, nullable=False)
    licencia = Column(String, nullable=False)
    consultorio_id = Column(Integer, ForeignKey("consultorios.id"), nullable=False)
    consultorio = relationship("Consultorio", back_populates="veterinarios")
    historias = relationship("HistoriaClinica", back_populates="veterinario")

class HistoriaClinica(Base):
    __tablename__ = "historias_clinicas"
    id = Column(Integer, primary_key=True)
    fecha_atencion = Column(Date, nullable=False)
    diagnostico = Column(String, nullable=False)
    tratamiento = Column(String, nullable=False)
    nombre_mascota = Column(String, nullable=False)
    veterinario_id = Column(Integer, ForeignKey("veterinarios.id"), nullable=False)
    veterinario = relationship("Veterinario", back_populates="historias")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("✅ Tablas creadas correctamente en clinica_veterinaria.db")