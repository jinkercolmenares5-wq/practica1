
import random

edad=random.randint(-50,50)


if edad < 0:
    print(f" el numero es {edad}")
    print("el numero es negativo")
else:
    print(f"la edad es {edad}")
    print("es positivo")


if edad %2 == 0:
    print(" es un numero par")
else:
    print("impar")


if edad >= 18:
    print("eres mayor de edad ")
else:
    print("eres menor de edad")

print("fin")


