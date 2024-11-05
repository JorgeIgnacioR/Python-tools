


def creolista():
    lista=[]
    lar=int(input("ingrese largo de la lista="))
    for i in range (lar):
        x=int(input("ingrese valor a la lista="))
        lista.append(x)
    return lista


def metodoburbujeo(lista):
    desordenado=True
    while desordenado:
        desordenado=False
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]:
                aux=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=aux
                desordenado=True
    return lista

def busquedabinaria(v,dato):
    izq=0
    der=len(a)-1
    pos=-1
    while izq<=der and pos==-1:
        centro=(izq+der)//2
        if v[centro]==dato:
            pos=centro
        elif v[centro]<dato:
            izq=centro+1
        else:
            der=centro-1
    return pos

def eliminarval(a,c):
    i=c
    del a[i]
    return a

def obtenervalormin(a):
    minimo=a[0]
    for i in range (len(a)-1):
        if a[i]<minimo:
            minimo=a[i]
    return minimo

a=creolista()
print(a)
print()


b=metodoburbujeo(a)
print(b)
print()

vbus=int(input("ingrese valor a buscar para eliminar"))
c=busquedabinaria(b,vbus)
print("la posciion donde se encuentra es en: ",end="")
print(c)
print()

d=eliminarval(b,c)
print("la lista con el valor eliminado queda:",end="")
print(d)
print()

h=obtenervalormin(a)
print("valor minimo:",end="")
print(h)