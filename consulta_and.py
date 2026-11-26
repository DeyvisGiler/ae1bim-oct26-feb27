# consulta_and.py
from configuracion import SessionLocal
from crear_base_entidades import HistoriaClinica, Veterinario
from sqlalchemy import and_

session = SessionLocal()

print(" Consulta con and(): Historias de Carlos posteriores al 2025-01-01 ")
resultados = session.query(HistoriaClinica).join(Veterinario).filter(
    and_(
        Veterinario.nombres == "Carlos",
        HistoriaClinica.fecha_atencion > "2025-01-01"
    )
).all()
for h in resultados:
    print(f"Mascota: {h.nombre_mascota} - Fecha: {h.fecha_atencion} - Diagnóstico: {h.diagnostico}")

session.close()