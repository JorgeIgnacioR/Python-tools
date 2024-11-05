import random

numero_secreto=random.randint(1,101)
intento=None

while intento !=numero_secreto:
    intento=int(input("ingrese el numero entre 1 y 100= "))
    if intento<numero_secreto:
        print("ingresa un numero mas grande")
    elif intento>numero_secreto:
        print("ingresa un numero mas bajo")

print("felicidades le pegaste")