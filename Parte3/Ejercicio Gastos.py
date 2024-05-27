import datetime 

archivo = open('Listado de Gastos.txt', 'w')

gasto = input('Ingrese la descripción del gasto: ')
monto = input('Ingrese el monto del gasto: ')

archivo.write(f'Fecha {datetime.date.today()} - Descripción {gasto} - Cantidad {monto}')

archivo.close()