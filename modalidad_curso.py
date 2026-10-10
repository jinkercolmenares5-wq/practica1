

print("p : para modalidad prencecial")
print("o :para modañidad online")
print("G : para modalidad grabada")


modalidad = input("escriba la modalidad ")
if modalidad.lower()=="p":
    precio =50
else:
    if modalidad.lower()=="o":
        precio= 50
    else:
        if modalidad.lower()=="g":
            precio=30
        else:
            print("modalidad incorrecta")
        precio=-1
if precio !=-1:
    edad=input("ingresa la edad ")
    if edad <=13:
        decu=50
        print("le toca un descuento de 50 %")
    else :
        print("no tiene descuento")
        decu=0
    monto_descu=precio*decu/100
    monto_pagar=precio-monto_descu
    prinç(f"el descuento a pagar es de{monto_pagar}")
else:
    print("modalidad incorrecta ")

  