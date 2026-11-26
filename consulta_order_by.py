# consulta_order_by.py
from configuracion import SessionLocal
from crear_base_entidades import Veterinario

session = SessionLocal()

print(" Consulta con order_by(): Veterinarios ordenados por apellido ")
resultados = session.query(Veterinario).order_by(Veterinario.apellidos).all()
for v in resultados:
    print(f"{v.apellidos}, {v.nombres} - Licencia: {v.licencia}")

session.close()