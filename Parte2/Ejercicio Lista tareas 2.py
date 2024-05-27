import json

def agregar_tareas(tareas, tarea):
    tareas.append(tarea)
    print(tareas)

def marcar_tarea(tareas, var1):
    tareas[var1-1] = tareas[var1-1] + ' okei' 
    

def mostrar_lista(tareas):
    for i, tarea in enumerate(tareas):
        print(f'{i + 1} ---> {tarea}')

try:
    with open ('Tareas pendientes.json', 'r') as archivo:
        tareas_pendientes = json.load(archivo)
except Exception as err:
    tareas_pendientes = []
    
while True:
    print('''
    1. Agregar tareas
    2. Marcar tarea como completada
    3. Mostrar las tareas pendientes
    4. Salir
          ''')
    try:
        opcion = input('Seleccione la opcion: ')
        if opcion == '1':
            tarea_agregar = input("Escriba la tarea que desea agregar: ")
            agregar_tareas(tareas_pendientes, tarea_agregar)
        elif opcion == '2':
            mostrar_lista(tareas_pendientes)
            tarea_a_marcar = int(input("Seleccione la tarea que desea marcar: "))
            marcar_tarea(tareas_pendientes, tarea_a_marcar)
        elif opcion == '3':
            mostrar_lista(tareas_pendientes)
        elif opcion == '4':
            break
        else:
            raise Exception()
    except:
       print('Opcion incorrecta')
with open('Tareas pendientes.json', 'w') as archivo:
    json.dump(tareas_pendientes,archivo, indent=4)
        