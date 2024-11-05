class Mesa:
    def __init__(self,numero, capacidad): #defino en su constructor nro de mesa y capacidad
        self.numero=numero
        self.capacidad=capacidad
        self.estado='libre'

    
    def reservar(self): #dice estado actual de las mesas
        if self.estado=='libre':
            self.estado='ocupada'
            return True #si no esta ocupada retorna true osea se puede servar
        return False #si esta ocupada retorna false osea no se puede reservar
        
        
    def liberar(self): #sirve para cuando se libera una mesa
        if self.estado =='ocupada':
            self.estado='libre' 
            return True #si esta ocupada y se libera retorna true
        return False #si estaba libre y la queremos liberar no se puede entonces retorna false


    def verificar_estado(self): #me retorna si la mesa esta libre u ocupada
        return self.estado


class Pedido:
    def __init__(self):
        self.items= [] #lista que se va a ir llenando con los pedidos
        self.estado= 'en preparacion'

    def agregar_item(self,item):
        self.items.append(item) #para agregar item a la lista

    def remover_item(self,item):
        if item in self.items:
            self.item.remove(item) #si quiero remover un item tiene que estar en la lista de items

    def calcular_total(self):
        return sum(item.precio for item in self.items)


    def cambiar_estado(self,nuevo_estado):
        self.estado= nuevo_estado #cambiar estado del pedido


class Menu:
    def __init__(self):
        self.items= []

    def agregar_item_al_menu(self, nombre, descripcion, precio):
        self.items.append(ItemMenu(nombre,descripcion,precio))

    def remover_item(self,nombre):
        self.item=[item for item in self.item if item.nombre !=nombre] #si no esta en la lista lo agrega si esta lo remueve

    def mostrar_menu(self):
        for item in self.items:
            print(f"{item.nombre}: {item.descripcion} - ${item.precio}") #recorremos item de la lista e imprimimos cada uno 


class ItemMenu:
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion= descripcion
        self.precio= precio


class Cliente:
    def __init__ (self, nombre):
        self.nombre = nombre
        self.mesa_asignada = None
        self.pedido_actual = Pedido()

    def asignar_mesa(self, mesa):
        self.mesa_asignada= mesa

    def realizar_pedido(self, items):
        for item in items:
            self.pedido_actual.agregar_item(item) #para ir agregando items al pedido

    def ver_cuenta(self):
        total=self.pedido_actual.calcular_total() #calculamos total para el pedido actual (funcion de calcular total en pedido)
        print(f"Total a pagar: ${total}")
        return total

class Restaurante:

    def __init__(self):
        self.mesas= []
        self.menu = Menu()
        self.clientes= []

    def anadir_mesa(self, numero, capacidad):  #crearemos metodo donde diremos numero de la mesa y su capacidad
        self.mesas.append(Mesa(numero, capacidad)) #Mesa viene de la clase mesa creada con anterioridad


    def remover_mesas (self, numero):
        self.mesas= [ mesa for mesa in self.mesas if mesa.numero !=numero] #me devuelve todas las mesas con numero distinto al que le entrego en el parametro

    
    def mostrar_mesas_disponibles(self):
        for mesa in self.mesas:
            if mesa.verificar_estado() == 'libre':
                print(f"Mesa {mesa.numero} (Capacidad: {mesa.capacidad}) esta disponible.")

    
    def hacer_reserva(self,cliente, numero_mesa):
        for mesa in self.mesas: #si mesa esta en la lista de mesas de nuestro restaurante
            if mesa.numero == numero_mesa and mesa.reservar(): #si el numero de la mesa es igual al nro de mesa que ingresamos como parametro y la mesa.reservar() osea es true ((osea esta libre))
                cliente.asignar_mesa(mesa) #le asignamos mesa al cliente
                self.clientes.append(cliente) #anadimos al cliente a la lista de clientes que inicialmente estaba vacia
                print(f" Mesa {numero_mesa} reservada para {cliente.nombre}.") #imprimimos mesa nro x esta reservada para el cliente x
                return True
        print(f"Mesa {numero_mesa} no esta disponible.") #y ahora ponemos que la mesa x ya no esta disponible porque ya la asignamos
        return False

    def gestionar_pedido(self, cliente, items):
        if cliente in self.clientes: #si el cliente ya tiene mesa
            cliente.realizar_pedido(items) #le agregamos items que el cliente quiere
            print(f"Pedido realizado para {cliente.nombre}.")
        else:
            print(f"Cliente no registrado.")

    def mostrar_menu(self):
        self.menu.mostrar_menu()


    def elegir_menu(self, cliente):
        if cliente in self.clientes:
            self.mostrar_menu()
            items_seleccionados= []
            while True:
                item_nombre= input("Ingrese el nombre del item que desea agregar (o 'fin' para finalizar pedido): ")
                if item_nombre.lower() == 'fin': #pasamos el nombre a minuscula y si es igual a fin terminamos
                    break
                item_encontrado = next((item for item in self.menu.items if item.nombre.lower() == item_nombre), None) #si no encuentra un item envia un none
                if item_encontrado:
                    items_seleccionados.append(item_encontrado)
                else:
                    print("item no encontrado, asegurese que su seleccion este entre las opciones")
            self.gestionar_pedido(cliente, items_seleccionados)
        else:
            print({"cliente no registrado"})
                

    
    def mostrar_cuenta(self, cliente):
        if cliente in self.clientes: #si el cliente esta en la lista de clientes del local
            cliente.ver_cuenta() #ver.cuenta para ver el total que corresponde a ese cliente
        else:
            print(f"Cliente no registrado")


#######################################################EJEMPLO DE USO############################################################################

#MESAS Y MENUS DEL RESTAURANT

restaurante= Restaurante()
restaurante.anadir_mesa(1,4) #numero de mesa y capacidad en el parametro
restaurante.anadir_mesa(2,2) #numero de mesa y capacidad en el parametro
restaurante.menu.agregar_item_al_menu('Pizza', 'La mejor pizza 4 quesos' , 10) #nombre, descripcion y precio en el paramtro
restaurante.menu.agregar_item_al_menu('Ensalada', 'Fresca ensalada ceasar' , 6) #nombre, descripcion y precio en el paramtro


#PEDIDO QUE EFECTUA EL SISTEMA DE RESERVAS

cliente= Cliente('Leo Messi')
print(f"Mesas disponibles")
restaurante.mostrar_mesas_disponibles()
print(f"Reserva efectuada:")
restaurante.hacer_reserva(cliente,1) #numero de mesa e el parametro
print(f"Mesas disponibles")
restaurante.mostrar_mesas_disponibles()
print(f"opciones de menu disponibles")
restaurante.elegir_menu(cliente)
restaurante.mostrar_cuenta(cliente)