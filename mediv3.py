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
nombre = input("\nNombre: ")
apellido = input("Apellido: ")
dni = int(input("Número de DNI (sin puntos): "))
borrar_pantalla()

print(f"""
      Hola, {nombre}, le agradecemos por elegir nuestros servicios.
      A continuación, verá nuestro menú de inicio. Por favor, ingrese el número de la opción que desea elegir.
        
    [1] Solicitar Turno 
    [2] Modificar Turno
    [0] Finalizar operación
      
      """)

opcionInicio = int(input("Ingrese el número de la opción: "))

def solicitarTurnos():
    print("""Ingresó la opción [1]. Cargando lista de especialidades...
          
          [1] Cardiología
          [2] Médico Clínico
          [3] Pediatría
          [4] Dermatología
          [5] Psicología

          """)
    opcionTurno = int(input("Ingrese el número de la opción: "))

    especialidades = {
        '1': 'Cardiología',
        '2': 'Médico Clínico',
        '3': 'Pediatría',
        '4': 'Dermatología',
        '5': 'Psicólogo'
        }

    if opcionTurno in especialidades:
            borrar_pantalla()
            print("="*75)
            print(f"Eligió la opción: {opcionTurno} ({especialidades[opcionTurno]})")
            print("A continuación, verá los horarios disponibles.")
            
            turnosOcupados = []
            print("\nA continuación, verá los horarios disponibles. Ingrese el número del horario que desea:\n")
            horarios = [
                        "[1]08:00 a 8:30",
                        "[2]09:00 a 9:30",
                        "[3]10:00 a 10:30",
                        "[4]11:00 a 11:30",
                        "[5]12:00 a 12:30",
                        "[6]13:00 a 13:30",
                        "[7]14:00 a 14:30",
                        "[8]15:00 a 15:30",
                        "[9]16:00 a 16:30",
                        "[10]17:00 a 17:30",
                        "[11]18:00 a 18:30",
                        "[0]Volver al menú anterior"
                    ]
            for i, horario in enumerate(horarios, 1):
                        if i in turnosOcupados:
                            print(f"{i}. {horario} (Ocupado)")
                        else:
                            print(f"{i}. {horario}")
            opcionHorario = int(input("Ingrese el número del horario que desea: "))

            while opcionHorario != 0:
                 if opcionHorario in turnosOcupados:
                      print("\nEl turno seleccionado ya está ocupado. Por favor, elija otro horario.")
                 else:
                      print(f"\nEligió la opción: {opcionHorario} ({horarios[opcionHorario - 1]})")
                      
                      dniConfirmacion = int(input("Confirme el turno ingresando su DNI: "))
                      while dniConfirmacion == dni:
                           if dniConfirmacion == dni:
                                print("\nUsted ha confirmado su turno correctamente, muchas gracias. Que tenga un buen día.")
                                turnosOcupados.append(opcionHorario)
                                break
                           else:
                                print("Usted no ha confirmado el turno correctamente. Reingrese su número de DNI: ")
                                dniConfirmacion = int(input("Confirme el turno ingresando su DNI: "))

if opcionInicio == 1:
     solicitarTurnos()
else:
        print("Eligió cerrar el programa...")
        feet = "Gracias por utilizar nuestros servicios. ¡Hasta luego!"
        print(feet.center(75,"="))
