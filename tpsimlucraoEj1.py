#Ejercicios simulacro
#Ejercicio 1:Escribir un programa que utilice funciones para:
#Cargar una lista de N elementos con números enteros entre 50 y 780 obtenidos al azar. El valor de N se ingresa por teclado.
#Ordenar la lista en forma ascendente utilizando cualquier método de ordenamiento estudiado.
#Pedir un dato al usuario y buscarlo con búsqueda binaria e informar su posición o -1 sino se encuentra.
#Luego eliminar de la lista, el valor minimo en todas sus posiciones.
#Imprimir por pantalla la lista luego de realizar cada tarea.

import random
import copy

#FUNCIONES
#funcion definir largo de lista y cargar valores random

def listarandom():
    x=int(input("ingrese el tamano de la lista="))
    lista=[]
    for i in range(x):
        lista.append(random.randint(50,780))
    return lista


#ordenar lista mediante burbujeo para luego llelvar a cabo la busqueda binaria

def ordenar(a):
    desordenado=True
    while desordenado:
        desordenado=False
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                aux=a[i]
                a[i]=a[i+1]
                a[i+1]=aux
                desordenado=True
    return a

#metodo de busqueda binaria

def busqueda_binaria(v,dato):
    izq=0
    der=len(v)-1
    pos=-1
    while izq<=der and pos==-1:
        centro=(der+izq)//2
        if v[centro]==dato:
            pos=centro
        elif v[centro]<dato:
            izq=centro+1
        else:
            der=centro-1
    return pos

#obtener valor minimo
def obtenerminimo(a):
    minimo=a[0]
    for i in range(len(a)-1):
        if a[i]<minimo:
            minimo=a[i]
    return minimo

#eliminar valor minimo

def eliminarminimo(a,b):
    minimo=b
    i=0
    while i<len(a):
        if a[i]==minimo:
            del a[i]
            i=i-1
        i=i+1
    return a



#PROGRAMA PRINCIPAL

a=listarandom()
print(a)
print()


b=ordenar(a)
print("lista ordenada=")
print(b)
print()

#dato a buscar
c=int(input("ingrese el dato a buscar="))

#busqueda del elemento
d=busqueda_binaria(b,c)

#si lo encuentra avisa, sino avisa que no esta
if  d==-1:
    print("no se encuentra el dato de busqueda")
else:
    print("resultado de busqueda: el dato",c,"se encuentra en la posicion",d,)
print()


#obtener valor minimo
e=obtenerminimo(b)

#eliminar valor minimo encontrado

f=eliminarminimo(b,e)

#imprimir valor minimo y l;ista final

print("el valor minimo es",e,"y la lista queda:")
print(f)