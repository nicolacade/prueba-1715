import json

def agregar_nota(calificaciones_alumnos, alumno, nota):
    if alumno in calificaciones_alumnos:
        calificaciones_alumnos[alumno].append(nota)
    else:    
        calificaciones_alumnos[alumno] = [nota]
   
def mostrar_notas(calificaciones_alumnos):
    if calificaciones_alumnos:
        for i, (valor, claves) in enumerate(calificaciones_alumnos.items()):
            print(f'\n--> {i + 1} Alumno: {valor.capitalize()}; Notas: {claves}')
    else:
        print('\nNo hay alumnos registrados aún.')
        

try:
    with open ('Notas de los Alumnos.json', 'r') as archivo:
        calificaciones_alumnos = json.load(archivo)
except Exception as err:
    calificaciones_alumnos = {}
    
while True:
    print('''
    1. Agregar Alumno y Nota
    2. Mostrar el listado completo
    3. Salir
          ''')
    try:
        opcion = input('Seleccione la opcion: ')
        if opcion == '1':
            alumno = input("Escriba el nombre del alumno a agregar: ").capitalize()
            nota = int(input("Escriba la nota a agregar: "))
            agregar_nota(calificaciones_alumnos, alumno, nota)
        elif opcion == '2':
            mostrar_notas(calificaciones_alumnos)
        elif opcion == '3':
            break
        else:
            raise Exception()
    except:
       print('Opcion incorrecta')
with open('Notas de los Alumnos', 'w') as archivo:
    json.dump(calificaciones_alumnos,archivo, indent=4)
        