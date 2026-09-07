from fastapi import FastAPI, HTTPException
from flask import json

app = FastAPI(
    title="API Ejercicios Python",
    description="API para resolver ejercicios de programación en Python",
    version="1.0.0",
    contact={"name": "Jeremy Rivera", "email": "jrc090928@gmail.com"},
)

curso = "Programación Agéntica con Python"
semestre = 9
nombre = "Jeremy Rivera"

persona = {
    "nombre": "Jeremy Rivera",
    "edad": 21,
    "carrera": "Ingeniería de Sistemas",
    "ciudad": "Barranquilla",
}


class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_total(self):
        return self.precio * self.cantidad


@app.get("/")
def inicio():
    return {
        "mensaje": "API de ejercicios",
        "rutas": [f"/ejercicio{i}" for i in range(1, 16)],
    }


@app.get("/ejercicio1")
def ejercicio1():
    return {"curso": curso, "semestre": semestre, "nombre": nombre}


@app.get("/ejercicio2")
def ejercicio2(a: float, b: float):
    resultado = {
        "suma": a + b,
        "resta": a - b,
        "multiplicacion": a * b,
    }

    if b == 0:
        resultado["division"] = "No permitida (división por cero)"
        resultado["division_entera"] = "No permitida (división por cero)"
        resultado["modulo"] = "No permitida (división por cero)"
    else:
        resultado["division"] = a / b
        resultado["division_entera"] = a // b
        resultado["modulo"] = a % b

    resultado["potencia"] = a**b
    return resultado


@app.get("/ejercicio3")
def ejercicio3(num: int):

    if num % 2 == 0:
        return {"mensaje": "El número es par", "numero": num}

    siguiente_par = num + 1

    return {"mensaje": "El número es impar", "siguiente_par": siguiente_par}


@app.get("/ejercicio4")
def ejercicio4():

    pares = []
    impares = []

    for i in range(1, 21):
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)

    return {"pares": pares, "impares": impares}


def multiplicar(a, b):
    return a * b


@app.get("/ejercicio5")
def ejercicio5(a: float = 7, b: float = 8):

    resultado = multiplicar(a, b)

    return {"producto": resultado}


@app.get("/ejercicio6")
def ejercicio6():
    return persona


@app.get("/ejercicio7")
def ejercicio7():

    datos = {}

    for clave, valor in persona.items():
        datos[clave] = valor

    return {"informacion_personal": datos}


@app.get("/ejercicio8")
def ejercicio8():

    producto = Producto("Audífonos Bluetooth", 129999, 10)

    return {
        "producto": {
            "nombre": producto.nombre,
            "precio": producto.precio,
            "cantidad": producto.cantidad,
        },
        "valor_total_inventario": producto.calcular_valor_total(),
    }


@app.get("/ejercicio9")
def ejercicio9():

    try:
        resultado = 10 / 2
    except ZeroDivisionError:
        raise HTTPException(
            status_code=400, detail="Error: división por cero no permitida"
        )

    return {"resultado": resultado}


@app.get("/ejercicio10")
def ejercicio10():
    numeros = list(range(1, 11))

    return {
        "lista_completa": numeros,
        "primer_elemento": numeros[0],
        "ultimo_elemento": numeros[-1],
        "cantidad": len(numeros),
    }


@app.get("/ejercicio11")
def ejercicio11():
    numeros = list(range(1, 11))

    numeros_duplicados = [n * 2 for n in numeros]

    return {"lista_original": numeros, "lista_duplicada": numeros_duplicados}


def comparar_numeros(a, b):

    if a > b:
        return f"El número mayor es {a}"
    elif b > a:
        return f"El número mayor es {b}"
    else:
        return "Ambos números son iguales"


@app.get("/ejercicio12")
def ejercicio12(a: float = 15, b: float = 22):
    resultado = comparar_numeros(a, b)

    return {"resultado": resultado}


@app.get("/ejercicio13")
def ejercicio13():
    try:
        with open("datos.txt", "r") as archivo:
            contenido = archivo.read()
        return {"contenido": contenido}
    except FileNotFoundError:
        raise HTTPException(
            status_code=404, detail="Error: el archivo datos.txt no existe"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al leer el archivo: {e}")


@app.get("/ejercicio14")
def ejercicio14():
    import json

    return {"json_persona": json.loads(json.dumps(persona))}


class ProductoInventario:

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_valor_inventario(self):
        return self.precio * self.cantidad
    
@app.get("/ejercicio15")
def ejercicio15():
    inventario = [
        ProductoInventario("Laptop", 1000000, 5),
        ProductoInventario("Mouse", 100000, 15),
        ProductoInventario("Teclado", 120000, 10),
    ]

    datos_exportar = []
    valor_total_global = 0

    for producto in inventario:

        valor_inv = producto.calcular_valor_inventario()

        valor_total_global += valor_inv

        datos_exportar.append(
            {
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": producto.cantidad,
                "valor_inventario": valor_inv,
            }
        )

    with open("inventario.json", "w", encoding="utf-8") as archivo:
        json.dump(datos_exportar, archivo, ensure_ascii=False, indent=4)

    return {
        "valor_total_global": valor_total_global,
        "datos_exportados": datos_exportar,
        "mensaje": "Datos exportados exitosamente al archivo 'inventario.json'.",
    }
