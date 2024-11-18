import os

def borrar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name in ("ce", "nt", "dos"):
        os.system("cls")

encabezado = "Clínica Médica 'Medinet'"
print(encabezado.center(75,"="))
print("""
\n ¡Bienvenido al sistema de Atención al Cliente de la Clínica Medinet!
Actualmente nos encontramos con alta demanda, sepa entender la falta de turnos.
A continuación, le pediremos que ingrese sus datos para una mejor atención. 
""")

print("="*75)

nombre = input("\nNombre >")
apellido = input("Apellido >")
dni = int(input("Número de DNI (sin puntos) >"))
print(f"Hola", nombre, "le agradecemos por elegir nuestros servicios.")


print("Por favor, ingrese el número de la opción que desea elegir: ")

def menu_inicio():
    print("""
    [1] Solicitar Turno 
    [2] Prepagas Asociadas
    [3] Modificar Turno
    [4] Precios de Consulta
    [0] Finalizar operación
    """)
    opcion_inicio = int(input("Ingrese una opción: "))

    while opcion_inicio != 0:
        if opcion_inicio == 1:
            borrar_pantalla()
            print("Eligió [1] 'Solicitar Turno'. Cargando alista de especialidades...")
            #lista de especialidades
        elif opcion_inicio == 2:
            borrar_pantalla()
            print("Eligió [2] 'Prepagas asociadas'. Cargando lista de prepagas...")
            prepagas()
        elif opcion_inicio == 3:
            borrar_pantalla()
            print("Eligió [3]. Cargando turnos agendados...")
            #turnos
        elif opcion_inicio == 4:
            borrar_pantalla()
            print("Eligió [4]. Cargando lista de precios de consulta...")
        else:
            print("===================Opción inválida===================")
        opcion_inicio = int(input("Ingrese una opción: "))
menu_inicio()

#solicitar turnos
def solicitar_turno():
    print("""
    [1] Cardiología
    [2] Traumatología
    [3] Médico Clínico
    [4] Dermatología
    [5] Psicología
    [0] < Volver al menú anterior
    """)
    opcion_turno = int(input("Ingrese una opción: "))

    if opcion_turno == 1:
            #a
    elif opcion_turno == 2:
            #b
    elif opcion_turno == 3:
            #c
    elif opcion_turno == 4:
            #d
    elif opcion_turno == 5:
            #e
    elif opcion_turno == 0:
        menu_inicio()
    else:
        print("===================Opción inválida===================")
        opcion_turno = int(input("Ingrese una opción: "))

#prepagas asociadas
def prepagas():
    print("""
    [-] Geleno
    [-] SencorSelud
    [-] Camic
    [0] < Volver al menú anterior
    """)
    opcion_salir = int(input("\n Ingrese la opción: "))
    if opcion_salir == 0:
        menu_inicio()
    else:
        print("===================Opción inválida===================")

#confirmar turno
def confirmacion():
    true_pass = dni
    confirm_pass = int(input("Ingrese su DNI para confirmar el turno: "))
    if confirm_pass == true_pass:
        print("¡Usted ha confirmado su turno correctamente!")
    else:
        print("Ingresó un DNI incorrecto")
    confirm_pass = int(input("Ingrese su DNI para confirmar el turno: "))

#modificar turno
#lista de precios


#final
feet = "Gracias por utilizar nuestros servicios. ¡Hasta luego!"
print(feet.center(75,"="))