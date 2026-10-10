import random

edad = random.randint(-5,10)
print(f"la edad es {edad}")
if edad<0:
elif edad<=2:
    print("es un bb")
elif edad<10:
     print("esw un niño")
elif edad<=17:
    print(" es un adolecente")
elif edad <=25:
    print("es un adulto joven")
elif edad<=55:
    print("es adulto")
elif edad<=75:
    print("la es un adulto mayor")
else :
    print("es un anciano")
     