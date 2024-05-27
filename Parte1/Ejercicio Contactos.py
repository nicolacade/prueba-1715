def agregar_contacto(agenda, nombre, telefono, correo):
    agenda[nombre] - {'Teléfono': telefono, 'Correo': correo}

def buscar_contacto(agenda, criterio):
    for nombre, info in agenda.items():
        if criterio in nombre or criterio == info[ 'Teléfono']:
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info[ 'Teléfono' ]}")
            print(f"Correo: {info[ 'Correo' ]}")
agenda = {}
while True:
    print("\n1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Salir")
    opcion = input ("Selecciona una opción: ")
    if opcion == '1':
        nombre = input("Ingresa el nombre del contacto: ")
        telefono = input("Ingresa el número de teléfono: ")
        correo = input("Ingresa el correo electrónico: ")
        agregar_contacto (agenda, nombre, telefono, correo)
        print("Contacto agregado.")
    elif opcion == '2':
        criterio = input("Ingresa el nombre o número de teléfono a buscar: ")
        buscar_contacto(agenda, criterio)
    elif opcion == '3':
        break