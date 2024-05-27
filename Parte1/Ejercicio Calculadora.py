class Calculadora:
    def __init__(self, numero1 , numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        resultado = numero1 + numero2
        print(f'La suma de {self.numero1} + {self.numero2} es {resultado}')

numeroA = int(input('Ingrese un número: '))
numeroB = int(input('Ingrese otro número: '))

suma = Calculadora(numeroA,numeroB)