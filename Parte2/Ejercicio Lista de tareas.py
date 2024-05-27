def agregar_tareas(anota, tareas):
    tareas.append(anota)

def tarea_completada(completo, tareas):
    if 0 <= completo < len(tareas):
        tareas[completo] = '✔' + tareas[completo]

    
def mostrar_lista(tareas):
    for i, tareas in enumerate(tareas):
        print(f'{i + 1} --> {tareas}')
    
    
usuario = int(input('Usted puede seleccionar estas opciones: \n 1. Agregar una tarea\n 2. Marcar una tarea completada\n 3. Listar las tareas pendientes\n 4. Salir\n *Por favor seleccione el numero que desea: '))
while usuario <= 0 or usuario >4:
    usuario = int(input('\n Ese numero no corresponde a las opciones, por favor ingrese una opcion valida:\n 1. Agregar una tarea\n 2. Marcar una tarea completada\n 3. Listar las tareas pendientes\n 4.Salir\n *Por favor seleccione el numero que desea: '))
tareas = ['pan', 'queso', 'salame']
if usuario == 1:
    tarea_nueva = input('Escriba que desea agregar: ')
    agregar_tareas(tarea_nueva, tareas)
elif usuario == 2:
    mostrar_lista(tareas)
    seleccion = int(input("Seleccione el numero de posicion de la lista que desea tildar: ")) -1 
    tarea_completada(seleccion, tareas)
print(tareas)

