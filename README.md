# Electiva Programación Agéntica - Angie Valera

# basic_python_br
Basic Python Introduction - Base Repo to fork

# Curso Básico–Completo de Python

## Tópico 1. Variables y tipos de datos

```python
nombre = "Angie"
edad = 30
activo = True
type(nombre)
```

---

## Tópico 2. Operadores

```python
a + b
a - b
a * b
a / b
a % b
a == b
a != b
a > b
a < b
and
or
not
```

---

## Tópico 3. Condicionales

```python
edad = 18

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor")
```

---

## Tópico 4. Listas, tuplas y diccionarios

```python
frutas = ["manzana", "pera"]
frutas.append("uva")

coord = (10, 20)

persona = {
    "nombre": "Ana",
    "edad": 25
}
```

---

## Tópico 5. Bucles

```python
for f in frutas:
    print(f)

i = 0
while i < 5:
    print(i)
    i += 1
```

---

## Tópico 6. Funciones

```python
def saludar(nombre):
    return "Hola " + nombre

def sumar(a, b=0):
    return a + b
```

---

## Tópico 7. Funciones lambda

```python
doble = lambda x: x * 2
```

---

## Tópico 8. Programación Orientada a Objetos

```python
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return "Hola soy " + self.nombre
```

---

## Tópico 9. Manejo de errores

```python
try:
    int("abc")
except:
    print("Error")
```

---

## Tópico 10. Manejo de archivos

```python
with open("data.txt", "w") as f:
    f.write("Hola")

with open("data.txt") as f:
    print(f.read())
```

---

## Tópico 11. Importar módulos

```python
import math
math.sqrt(16)
from math import sqrt
```

---

## Tópico 12. Comprensión de listas

```python
numeros = [x*2 for x in range(5)]
```

---

## Tópico 13. JSON

```python
import json

data = {"nombre": "Ana"}
json.dumps(data)
json.loads('{"edad":30}')
```

---

## Tópico 14. Taller práctico (Al final de cada uno mostrar en pantalla el resultado)

1. Crear variable curso, semestre, nombre
2. Solicite dos números al usuario. Muestre el resultado de la suma, resta, multiplicación, división, división entera, módulo y potencia.
3. Solicite un número entero. Validar si es par, muestre el mensaje "El número es par". Si es impar, conviértalo al siguiente número par y muestre el resultado.
4. Utilice un ciclo for para imprimir los números del 1 al 20. Indique cuáles son pares y cuáles son impares.
5. Cree una función multiplicar(a, b) que reciba dos números y retorne su producto. Llame la función e imprima el resultado.  
6. Cree un diccionario persona con las claves nombre, edad, carrera y ciudad y muestre toda su información.
7. Recorra el diccionario persona mostrando sus claves, sus valores y cada par clave–valor.
8. Cree una clase Producto con los atributos nombre, precio y cantidad, agregue un método para calcular el valor total del inventario y muestre el resultado.
9. Solicite dos números y realice una división utilizando try/except para manejar divisiones por cero o entradas inválidas.
10. Cree una lista con los números del 1 al 10 y muestre la lista completa, el primer elemento, el último y la cantidad de elementos.
11. Cree una nueva lista a partir de la anterior donde cada número esté duplicado y muestre ambas listas.
12. Cree una función que reciba dos números y muestre cuál es el mayor o indique si ambos son iguales.
13. Lea el contenido de un archivo datos.txt utilizando manejo de excepciones y muestre el contenido o el mensaje de error correspondiente.
14. Convierta el diccionario persona a formato JSON utilizando el módulo json y muestre el resultado en pantalla.
15. Cree una lista con tres objetos de la clase Producto, calcule el valor total del inventario y exporte la información a un archivo JSON.

---

