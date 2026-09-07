try:
    with open("datos.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
except FileNotFoundError:
    print("Error: El archivo 'datos.txt' no existe.")
except Exception as e:
    print(f"Ocurrió un error inesperado al leer el archivo: {e}")
