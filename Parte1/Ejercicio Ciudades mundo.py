def buscar_ciudad(ciudades_info, valor1):
    for i in ciudades_info:
        if valor1.lower() == i.lower():
            return ciudades_info[i]
    
def mostrar_ciudad(valor1,valor2):
    lista = []
    for i, (valor,clave) in enumerate(valor2.items()):
        lista.append(clave)
    print(f'La ciudad de {valor1} pertenece a {lista[0]} cuenta con una poblacion de {lista[1]} y sus mayores atracciones son la {','.join(lista[2])}')
ciudades_info = {
    'Paris': {
        'Pais': 'Francia',
        'Poblacion': 2187526,
        'Puntos_de_Interes': ['Torre Eiffel',
'Louvre', 'Catedral de Notre-Dame']
    },
    'Nueva York': {
        'Pais': 'Estados Unidos',
        'Poblacion': 8398748,
        'Puntos_de_Interes': ['Estatua de la Libertad', 
'Central Park', 'Times Square']
    },  
    'Tokio': {
        'Pais': 'Japón',
        'Poblacion': 13929286,
        'Puntos _de_Interes': ['Torre de Tokio',
'Templo Senso-ji', 'Palacio Imperial']
    }
}
try:
    ciudad_busqueda = input('Ingrese el nombre de la ciudad que desea buscar: ')
    mostrar_ciudad(ciudad_busqueda, buscar_ciudad(ciudades_info, ciudad_busqueda))
except:
    print('La ciudad ingresada no existe, vuelva a intentarlo')