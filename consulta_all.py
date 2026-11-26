# consulta_all.py
from configuracion import SessionLocal
from crear_base_entidades import Clinica

session = SessionLocal()

print(" Consulta con all(): Clínicas y número de Historias Clínicas ")
clinicas = session.query(Clinica).all()
for clinica in clinicas:
    total = 0
    for consultorio in clinica.consultorios:
        for veterinario in consultorio.veterinarios:
            total += len(veterinario.historias)
    print(f"Clínica: {clinica.nombre} → Historias Clínicas: {total}")

session.close()