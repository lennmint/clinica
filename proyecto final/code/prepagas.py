#clinica

#menu de prepagas
import pandas as pd
df = pd.read_excel (r"C:\Users\Ayelen\Documents\Coding\proyecto final\excel\datos_prepagas.xls")
print(df)



#input del usuario
ingresoOpcion = True
while ingresoOpcion == True:
    opcion = input("elija la opcion --> ")
    match opcion:
        case "0":
            print("\n USTED ELIGIÓ HOMINIS COMO SU PREPAGA")
        case "1":
            print("\n USTED ELIGIÓ PREMEDIC COMO SU PREPAGA")
        case "2":
            print("\n USTED ELIGIÓ SANCOR COMO SU PREPAGA")
        case "3":
            print("\n USTED ELIGIÓ AVALAIN COMO SU PREPAGA")
        case "4":
            print("\n USTED ELIGIÓ GALENO COMO SU PREPAGA")
        case "5": 
            print("\n USTED ELIGIÓ OSDE COMO SU PREPAGA")
        case "9":
            print("\n SALIR DEL MENU")
            ingresoOpcion = False
        case _:
            print("\n OPCION EQUIVOCADA, VUELVA A INTENTARLO")