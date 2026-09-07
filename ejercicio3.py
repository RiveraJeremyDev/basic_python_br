num= int(input("Ingrese un número entero: "))

if num % 2 == 0:
    print("El número es par")
else:
    siguiente_par = num + 1
    print("El número es impar")
    print("El siguiente número par es:", siguiente_par)