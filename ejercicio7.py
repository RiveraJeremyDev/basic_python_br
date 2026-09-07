persona = {
    "nombre": "Jeremy Gyomatt Rivera Chico",
    "edad": 21,
    "carrera": "Ingeniería de Software",
    "ciudad": "Barranquilla",
}

print("Información personal:")
for clave, valor in persona.items():
    print(f"- {clave.capitalize()}: {valor}")