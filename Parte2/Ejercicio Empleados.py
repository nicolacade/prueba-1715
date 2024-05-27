class Empleado:
   
    def __init__(self, nombre, apellido, edad, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = salario  
    
    def mostrar_informacion(self):
        return f'El empleado {self.nombre} {self.apellido} tiene {self.edad} y gana {self.salario}'

    def aumentar_salario(self, porcentaje):
        sueldo_nuevo = (self.salario * porcentaje) // 100
        return f' Se le aumento un {porcentaje}% y ahora gana {self.salario + sueldo_nuevo}'        

class Gerente(Empleado):
    def __init__(self, nombre, apellido, edad, salario, departamento):
        super().__init__(nombre, apellido, edad, salario)
        self.departamento = departamento
    
    def mostrar_informacion(self):
        return f'El empleado {self.nombre} {self.apellido} tiene {self.edad} y gana {self.salario} y es del sector {self.departamento}'

    


empleado1 = Empleado('Nicolas', 'Vilgre', 32, 2000)
empleado2 = Empleado('Silvina', 'Sffaeir', 33, 6000)
gerente1 = Gerente('Isabella', 'Sasa', 48, 9000, 'Ventas')

print(empleado1.mostrar_informacion())
print(empleado2.mostrar_informacion())
print(empleado1.aumentar_salario(100))
print(gerente1.mostrar_informacion())