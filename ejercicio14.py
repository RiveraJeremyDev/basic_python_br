import json

persona = {
    "nombre": "Jeremy Gyomatt Rivera Chico",
    "edad": 21,
    "carrera": "Ingeniería de Software",
    "ciudad": "Barranquilla",
}

persona_json = json.dumps(persona, ensure_ascii=False, indent=4)
print("Diccionario convertido a JSON:")
print(persona_json)
