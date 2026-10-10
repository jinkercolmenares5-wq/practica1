edad= int(input("ingresa la edad :"))


entrada=1000
dia_semana=input("ingrese que dia de la semana es ")
if dia_semana.lower()=="lunes":
    print("todos tiene el 50 %")
    descuento=50


if edad<=2:
    descuento=100
elif edad<=5:
    descuento=50
elif edad<=10:
    descuento=20
elif edad<55:
    descuento=0
else :
    descuento=30

if descuento<30:
    estudiante=input("es un estuasiabte (si o no ) :")
    if estudiante.lower()=="si":
        descuento=25

if descuento != 0:
    descuento= entrada*descuento/100
    print(f"el descuento es de { descuento}")
    print(f"el monto del descuento { descuento}")

else :
    descuento=0

monto_pagar= entrada-descuento

print(f" el monto a pagar ; { monto_pagar}")

