try:
    edad = int(input('Ingrese su edad: '))
    if edad >= 18 and edad<= 65:
        print('La edad es correcta.')
except ValueError:
    print('No es un número válido')
except :
    ...