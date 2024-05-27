class CarritoCompras():
    
    cantidad_total_productos = 0
    
    def __init__(self):
        self.listado_productos = []
    
    def agregar_productos(self):
        nombre = input('\nIngrese el nombre del producto que desea agregar: ')
        precio = input('Ingrese el precio: ')
        cantidad_disponible= input('Ingrese la cantidad: ')
        codigo_producto = input('Ingrese el codigo del producto: ')
        if len(nombre) == 0 or len(precio) == 0 or len(cantidad_disponible) == 0 or len(codigo_producto) == 0:
            print('\nNo se pueden cargar campos vacíos, intentelo nuevamente.')
        else:
            self.listado_productos.append(Producto)
            print('\nEl producto se ha agregado correctamente. ')
            
    def eliminar_productos(self):
        producto_eliminar = input('Ingrese el nombre del producto que desea eliminar: ')
        for i in self.listado_productos:
            if i == producto_eliminar:
                self.listado_productos.remove(producto_eliminar)
            else:
                print('No existe el producto buscando')
    
    def calcular_total():
        ...
    def menu(self):
        repetir_menu = True
        while repetir_menu:
            print('''
            ---------------------
                    MENU
            ---------------------
            1. Agregar un producto
            2. Eliminar un producto
            3. Calcular el total de la compra
            4. Salir
            ''')
            opcion = input ("Selecciona una opción: ")
            if opcion == '1':
                self.agregar_productos()
            elif opcion == '2':
                self.eliminar_productos()
            elif opcion == '3':
                self.calcular_total()
            elif opcion == '4':
                repetir_menu = False
                print('Finalizó el programa.')
            else:
                print('La opción ingresada no es válida.')

class Producto(CarritoCompras):
    
    def __init__(self, nombre, precio, cantidad_disponible, codigo_producto):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
        self.codigo_producto = codigo_producto

                
cliente1 = CarritoCompras()
cliente1.menu()