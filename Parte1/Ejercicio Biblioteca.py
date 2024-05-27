class Libro():
    
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.disponible = True

class Biblioteca():
    
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro_a_agregar):
        self.libros.append(libro_a_agregar)
    
    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False
                return f'El libro {titulo} se retiró'
        return f'El libro {titulo} no está disponible'
    
    def devolver_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = True
                return f'El libro {titulo} se devolvió'
        return f'El libro {titulo} no puede ser devuelto'
    
    def mostrar_libros(self):
        disponibles = [libro.titulo for libro in self.libros if libro.disponible]
        return f'Los libros que hay son: {','.join(disponibles)}'
    
        
libro1 = Libro('El gran Gatsby', 'Fitzgerald', 1925)
libro2 = Libro('Cien años de soledad', 'Gabriel Garcia Marquez', 1967)
biblioteca = Biblioteca()

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

print(biblioteca.prestar_libro('El gran Gatsby'))
print(biblioteca.devolver_libro('El gran Gatsby'))
print(biblioteca.mostrar_libros())