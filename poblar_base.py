# poblar_base.py
from configuracion import SessionLocal
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica
from datetime import date

session = SessionLocal()

# Clínicas
clinica1 = Clinica(nombre="VetSalud Norte", direccion="Av. Principal 123", medico_responsable="Dra. Ana Pérez")
clinica2 = Clinica(nombre="AnimalCare Sur", direccion="Calle 45 #67-89", medico_responsable="Dr. Luis Gómez")
session.add_all([clinica1, clinica2])
session.commit()

# Consultorios
cons1 = Consultorio(nombre="Consultorio 1", especialidad="Medicina General", clinica_id=clinica1.id)
cons2 = Consultorio(nombre="Consultorio 2", especialidad="Cirugía", clinica_id=clinica1.id)
cons3 = Consultorio(nombre="Consultorio A", especialidad="Dermatología", clinica_id=clinica2.id)
session.add_all([cons1, cons2, cons3])
session.commit()

# Veterinarios
vet1 = Veterinario(nombres="Carlos", apellidos="Ramírez", email="carlos@vet.com", licencia="LIC-001", consultorio_id=cons1.id)
vet2 = Veterinario(nombres="María", apellidos="López", email="maria@vet.com", licencia="LIC-002", consultorio_id=cons1.id)
vet3 = Veterinario(nombres="Jorge", apellidos="Silva", email="jorge@vet.com", licencia="LIC-003", consultorio_id=cons2.id)
vet4 = Veterinario(nombres="Laura", apellidos="Torres", email="laura@vet.com", licencia="LIC-004", consultorio_id=cons3.id)
session.add_all([vet1, vet2, vet3, vet4])
session.commit()

# Historias clínicas
hist1 = HistoriaClinica(fecha_atencion=date(2025, 1, 10), diagnostico="Otitis", tratamiento="Antibiótico", nombre_mascota="Firulais", veterinario_id=vet1.id)
hist2 = HistoriaClinica(fecha_atencion=date(2025, 1, 15), diagnostico="Fractura", tratamiento="Yeso", nombre_mascota="Michi", veterinario_id=vet1.id)
hist3 = HistoriaClinica(fecha_atencion=date(2025, 2, 1), diagnostico="Dermatitis", tratamiento="Crema", nombre_mascota="Rex", veterinario_id=vet2.id)
hist4 = HistoriaClinica(fecha_atencion=date(2025, 2, 10), diagnostico="Vacunación", tratamiento="Vacuna", nombre_mascota="Luna", veterinario_id=vet4.id)
session.add_all([hist1, hist2, hist3, hist4])
session.commit()

session.close()
print(" Datos insertados correctamente.")