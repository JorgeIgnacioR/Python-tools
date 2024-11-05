#Objetivo:
#Escribir una función que reciba como
#parámetros la fecha de nacimiento de
#una persona y la fecha actual, y
#devuelva la edad de la persona.


def calcularedad(dianac,mesnac,añonac,diaact,mesact,añoact):
    edad=añoact-añonac
    if mesact < mesnac:
        edad=edad-1
    elif mesact==mesnac and diaact<dianac:
        edad=edad-1
    return edad
    
    

dianac=int(input("ingrese dia de nacimiento= "))
mesnac=int(input("ingrese mes de nacimiento= "))
añonac=int(input("ingrese año de nacimiento= "))
diaact=int(input("ingrese dia actual= "))
mesact=int(input("ingrese mes actual= "))
añoact=int(input("ingrese año actual= "))
edad_final=calcularedad(dianac,mesnac,añonac,diaact,mesact,añoact)
print(edad_final)   



