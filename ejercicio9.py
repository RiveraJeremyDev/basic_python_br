try:
    num1 = float(input("Ingrese el numerador: "))
    num2 = float(input("Ingrese el denominador: "))
    division = num1 / num2
    print(f"El resultado de la división es: {division}")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Debe ingresar un valor numérico válido.")
