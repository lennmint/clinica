import pandas as pd

print("______________________________________________________")
esp = pd.read_excel (r"C:\Users\Ayelen\Documents\Coding\proyecto final\excel\clínica.xls", sheet_name="especialidades")
print(esp)

print("______________________________________________________")
Inputopcion2 = True
while Inputopcion2 == True:
    opcion2 = input("Ingrese una opción: ")
    print("______________________________________________________")
    match opcion2:
         case "0":
            franjas_horarias = pd.read_excel (r"C:\Users\Ayelen\Documents\Coding\proyecto final\excel\clínica.xls", sheet_name="fh_0")
            print(franjas_horarias)
            opcion=input("Seleccione el horario deseado: ")
            match opcion:
                case "0":
                    print("Su turno será a las 08:00AM")
                case "1":
                    print("Su turno será a las 12:30PM")
                case "2":
                    print("Saliendo")
                    Inputopcion2=False
         case "1":
            franjas_horarias = pd.read_excel (r"C:\Users\Ayelen\Documents\Coding\proyecto final\excel\clínica.xls", sheet_name="fh_1")
            print(franjas_horarias)
         case "2":
            franjas_horarias = pd.read_excel (r"C:\Users\Ayelen\Documents\Coding\proyecto final\excel\clínica.xls", sheet_name="fh_2")
            print(franjas_horarias)
         case "3":
            franjas_horarias = pd.read_excel (r"C:\Users\Ayelen\Documents\Coding\proyecto final\excel\clínica.xls", sheet_name="fh_3")
            print(franjas_horarias)
         case "4":
              print("Volviendo al menú anterior...")
              Inputopcion2 = False