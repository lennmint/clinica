#clinica_intro
import pandas as pd

print("\n ¡Bienvenido a Lorem Ipsum! Le agradecemos por elegir nuestros servicios")
usuario = input("Ingrese su Nombre y Apellido: ")
dni = input("Ingrese su número de DNI: ")
print("\n Hola", usuario, "seleccioná la opción que necesitas: ")

menu1 = pd.read_excel (r"C:\Users\Ayelen\Documents\Coding\proyecto final\excel\menu1.xls")
print(menu1)

opcion = input("elija la opcion --> ")

match opcion:
    case "0":
        print("______________________________________________________")
        especialidades = pd.read_excel (r"C:\Users\Ayelen\Documents\Coding\proyecto final\excel\especialidades.xls")
        print(especialidades)
        opcion2 = input("La especialidad que deseo es: ")
        match opcion2:
            case "0":
                franjas_horarias = pd.read_excel (r"C:\Users\Ayelen\Documents\Coding\proyecto final\excel\franjas horarias.xls")
                print(franjas_horarias)
