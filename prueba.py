
import random
import copy


'''FUNCIONES'''
#creo lista
def creolista():
    lista=[]
    for i in range(12):
        lista.append(random.randint(0,100))
    return lista

#reemplazoelemento
def posyrem(lista):
    largo=len(lista)
    pos=int(input("ingrese posicion a reemplazar="))
    while pos>len(lista) or pos<0:
        pos=int(input("reingrese posicion a reemplazar="))
    val=int(input("ingrese valor a reemplazar="))
    lista[pos]=val
    return lista
    
    
    
#ordeno por burbujeo
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
                
                
        
#busqueda binaria
def busquedabinaria(v,dato):
    izq=0
    der=len(lista)-1
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

    
#obtener valor minimo
def obtenerminimo(lista):
    minimo=lista[0]
    for i in range(len(lista)-1):
        if lista[i]<minimo:
            minimo=lista[i]
    return minimo

        
#eliminar valor
def eliminarminimo(a,b):
    minimo=g
    i=0
    while i<len(lista):
        if lista[i]==minimo:
            del lista[i]
            i=i-1
        i=i+1
    return lista
    
    

'''PROGRAMA PRINCIPAL'''

lista=creolista()
if len(lista)>0:
    print(lista)
    print()
    
    #BUSCOPOS Y REEMPLAZO
    b=posyrem(lista)
    print(b)
    print()
    
    #ORDENAMIENTO
    print("Lista ordenada")
    c=metodoburbujeo(lista)
    print(c)
    print()
    
    #BUSQUEDA BINARIA
    d=int(input("ingrese dato a buscar="))
    
    e=busquedabinaria(lista,d)
    
    if e==-1:
        print("no se encontro el valor buscado")
    else:
        print("el dato",d,"se encuentra en la pos",e,)
    print()
    
    #OBTENER MINIMO
    print("el minimo de la lista es=",end="")
    g=obtenerminimo(lista)
    print(g)
    print()
    
    #ELIMINAR VALOR MINIMO
    print("la lista con el minimo eliminado es:",end="")
    h=eliminarminimo(lista,g)
    print(h)
    
else:
    print("no se ingresaron valores")

