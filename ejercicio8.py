class Producto:

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad


# Ejemplo de uso
prod1 = Producto("Audífonos Bluetooth", 129999, 10)
print(
    f"El valor total del inventario de {prod1.nombre} es: ${prod1.calcular_valor_total()}"
)