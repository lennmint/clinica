import pandas as pd

print("______________________________________________________")
esp = pd.read_excel (r"C:\Users\Ayelen\Documents\Coding\proyecto final\excel\especialidades.xls")
print(esp)

print("______________________________________________________")
Inputopcion2 = True
while Inputopcion2 == True:
    opcion2 = input("Ingrese una opción: ")
    match opcion2:
         case "0":
            franjas_horarias = pd.read_excel (r"C:\Users\Ayelen\Documents\Coding\proyecto final\excel\franjas horarias.xls")
            print(franjas_horarias)
         case "1":
            franjas_horarias = pd.read_excel (r"C:\Users\Ayelen\Documents\Coding\proyecto final\excel\franjas horarias.xls")
            print(franjas_horarias)
         case "2":
            franjas_horarias = pd.read_excel (r"C:\Users\Ayelen\Documents\Coding\proyecto final\excel\franjas horarias.xls")
            print(franjas_horarias)
         case "3":
            franjas_horarias = pd.read_excel (r"C:\Users\Ayelen\Documents\Coding\proyecto final\excel\franjas horarias.xls")
            print(franjas_horarias)
         case "4":
              print("Volviendo al menú anterior...")
              Inputopcion2 = False