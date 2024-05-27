def agregar_usuario(usuarios_contraseñas, usuario_a_agregar, contraseña_a_agregar):
    while len(usuario_a_agregar) == 0 or len(contraseña_a_agregar) == 0:
        print('\nNo se puede registrar usuario o contraseña vacío')
        usuario_a_agregar = input("\nVuelva a ingresar el usuario nuevo: ")
        contraseña_a_agregar = input("Ingrese la contraseña para el usuario: ")
    for i, (clave,valor) in enumerate(usuarios_contraseñas.items()):
        if usuario_a_agregar == clave:
            print('\nEl usuario ya existe')
            break
    else:
        usuarios_contraseñas[usuario_a_agregar] = contraseña_a_agregar
        print("\nEl usuario se agregó correctamente.")
        print('-' * 60)
def mostrar_listado():
    for i, (clave,valor) in enumerate(usuarios_contraseñas.items()):
        print(f'\n{i + 1} --> Usuario: {clave} --- contraseña: {valor}')
def busqueda_usuario(usuarios_contraseñas, usuario_a_buscar, contraseña_a_buscar):
    for clave in usuarios_contraseñas:
        if clave.lower() == usuario_a_buscar.lower():
            if usuarios_contraseñas[clave] == contraseña_a_buscar:
                return 'Has iniciado sesión correctamente.'
            else:
                return 'La contraseña ingresada es incorrecta.'
    else:
        return 'El usuario ingresado no existe.'
        
usuarios_contraseñas = {}
while True:
    print('''
    SISTEMA DE REGISTRO.

    Usted puede elegir entre las siguientes opciones:
    1. Registrar un usuario nuevo.
    2. Ingresar en el sistema.
    3. Mostrar el listado completo de los usuarios registrados.
    4. Salir.
    ''')
    try:
        opcion = input("Seleccione el numero de la opción que desea: ")
        if opcion == '1':
            print('\nRegistrar un nuevo usuario:')
            usuario = input("Ingrese el usuario nuevo: ")
            contraseña = input("Ingrese la contraseña para el usuario: ")
            agregar_usuario (usuarios_contraseñas, usuario, contraseña)
        elif opcion == '2':
            print('\nAcceso al sistema.')
            usuario_login = input("Ingrese el usuario: ")
            contraseña_login = input("Ingrese la contraseña: ")
            print(f'\n{busqueda_usuario(usuarios_contraseñas, usuario_login, contraseña_login)}')
            print('-' * 60)
        elif opcion == '3':
            if len(usuarios_contraseñas) == 0:
                print('No hay usuarios registrados hasta el momento')
                print('-' * 60)
            else:
                print('\nEste es el listado completo de usuarios registrados hasta el momento: ')
                mostrar_listado()
                print('-' * 60)
        elif opcion == '4':
            print('\nSalió del sistema correctamente')
            print('-' * 60)
            break
        else:
            raise Exception()
    except:
        print('\nLa opción ingresada es incorrecta, por favor vuelva a intentarlo')
        print('-' * 60)