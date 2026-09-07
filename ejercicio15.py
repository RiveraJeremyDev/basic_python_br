import json


class Producto:

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_valor_inventario(self):
        return self.precio * self.cantidad


inventario = [
    Producto("Laptop", 1000000, 5),
    Producto("Mouse", 100000, 15),
    Producto("Teclado", 120000, 10),
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

print(f"Valor total global del inventario: ${valor_total_global}")

with open("inventario.json", "w", encoding="utf-8") as archivo:
    json.dump(datos_exportar, archivo, ensure_ascii=False, indent=4)

print("Datos exportados exitosamente al archivo 'inventario.json'.")
