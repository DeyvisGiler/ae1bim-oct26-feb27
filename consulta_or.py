# consulta_or.py
from configuracion import SessionLocal
from crear_base_entidades import Clinica
from sqlalchemy import or_

session = SessionLocal()

print("=== Consulta con or(): Clínicas con responsable Ana o Luis ===")
resultados = session.query(Clinica).filter(
    or_(
        Clinica.medico_responsable.like("%Ana%"),
        Clinica.medico_responsable.like("%Luis%")
    )
).all()
for c in resultados:
    print(f"{c.nombre} - Responsable: {c.medico_responsable}")

session.close()