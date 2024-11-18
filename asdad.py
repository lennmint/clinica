# Crear un diccionario con dos columnas
mi_diccionario = {
    'Columna1': [1, 2, 3],
    'Columna2': ['A', 'B', 'C']
}

# Acceder a los valores de las columnas
print(mi_diccionario['Columna1'])  # Imprime: [1, 2, 3]
print(mi_diccionario['Columna2'])  # Imprime: ['A', 'B', 'C']


# Datos de las columnas
columna1 = [1, 2, 3]
columna2 = ['A', 'B', 'C']

# Combinar las columnas
for valor1, valor2 in zip(columna1, columna2):
    print(f"{valor1} - {valor2}")

__


user_dict = {}
num_entries = int(input("Ingresa la cantidad de entradas que deseas agregar: "))
for i in range(num_entries):
    key = input("Ingresa la clave: ")
    value = input("Ingresa el valor: ")
    user_dict[key] = value
print("Diccionario después de agregar datos del usuario:", user_dict)


'''
Ingresa la cantidad de entradas que deseas agregar: 4
Ingresa la clave: adarsh
Ingresa el valor: 12
Ingresa la clave: raj
Ingresa el valor: 10
Ingresa la clave: Aditya
Ingresa el valor: 10
Ingresa la clave: Anish
Ingresa el valor: 11
Diccionario después de agregar datos del usuario: {'adarsh': '12', 'raj': '10', 'Aditya': '10', 'Anish': '11'}

'''


num_entries = int(input("Ingresa la cantidad de entradas que deseas agregar: "))
user_dict = {input(f"Ingresa la clave {i+1}: "): input(f"Ingresa el valor {i+1}: ") for i in range(num_entries)}
print("Diccionario después de agregar datos del usuario:", user_dict)

'''
Ingresa la cantidad de entradas que deseas agregar: 2
Ingresa la clave 1: Adarsh
Ingresa el valor 1: 12
Ingresa la clave 2: Raj
Ingresa el valor 2: 10
Diccionario después de agregar datos del usuario: {'Adarsh': '12', 'Raj': '10'}

'''
user_dict = {}
num_entries = int(input("Ingresa la cantidad de entradas que deseas agregar: "))
for i in range(num_entries):
    key = input("Ingresa la clave: ")
    value = input("Ingresa el valor: ")
    user_dict.update({key: value})
print("Diccionario después de agregar datos del usuario:", user_dict)

'''
Ingresa la cantidad de entradas que deseas agregar: 3
Ingresa la clave: nombre
Ingresa el valor: María
Ingresa la clave: edad
Ingresa el valor: 30
Ingresa la clave: ciudad
Ingresa el valor: Madrid
Diccionario después de agregar datos del usuario: {'nombre': 'María', 'edad': '30', 'ciudad': 'Madrid'}

'''