# consulta_filter.py
from configuracion import SessionLocal
from crear_base_entidades import Consultorio

session = SessionLocal()

print("=== Consulta con filter(): Consultorios de Cirugía ===")
resultados = session.query(Consultorio).filter(Consultorio.especialidad == "Cirugía").all()
for c in resultados:
    print(f"{c.nombre} - Especialidad: {c.especialidad}")

session.close()