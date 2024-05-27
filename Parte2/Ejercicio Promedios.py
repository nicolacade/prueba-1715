def calcular_promedio(*lista_notas):
    promedio = 0
    for i in lista_notas:
        promedio = promedio + i
    promedio_final = promedio / len(lista_notas)
    return promedio_final
lista_notas = []
while True:
    print('''
    1. Agregar nota
    2. Sacar promedio
    3. Salir
          ''')
    opcion = input('Seleccione la opcion: ')
    if opcion == '1':
        nota = float(input("Escriba la tarea que desea agregar: "))
        lista_notas.append(nota)
    elif opcion == '2':
        print(f'El promedio es: {calcular_promedio(*lista_notas)}')
    elif opcion == '3':
        break