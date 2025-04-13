import os
import json


def borrar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name in ("ce", "nt", "dos"):
        os.system("cls")


archivo_json = 'usuarios.json'
archivo_turnos = 'turnos.json'


def cargar_usuarios():
    if os.path.exists(archivo_json):
        with open(archivo_json, 'r') as file:
            return json.load(file)
    return {}


def guardar_usuarios():
    with open(archivo_json, 'w') as file:
        json.dump(personas, file, indent=4)


personas = cargar_usuarios()


def cargar_turnos():
    if os.path.exists(archivo_turnos):
        with open(archivo_turnos, 'r') as file:
            return json.load(file)
    return {especialidad: [] for especialidad in especialidades.values()}


def guardar_turnos():
    with open(archivo_turnos, 'w') as file:
        json.dump(turnosOcupados, file, indent=4)


especialidades = {
    '1': 'Cardiología',
    '2': 'Médico Clínico',
    '3': 'Pediatría',
    '4': 'Dermatología',
    '5': 'Psicología'
}




turnosOcupados = cargar_turnos()




horarios = [
    "08:00 a 08:30",
    "09:00 a 09:30",
    "10:00 a 10:30",
    "11:00 a 11:30",
    "12:00 a 12:30",
    "13:00 a 13:30",
    "14:00 a 14:30",
    "15:00 a 15:30",
    "16:00 a 16:30",
    "17:00 a 17:30",
    "18:00 a 18:30",
]




def ingresoSistema():
    dni = input("Ingrese el DNI: ")
    if dni in personas.keys():
        print("Ese DNI ya fue cargado...")
    else:
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = int(input("Edad: "))
        obraSocial = input("Obra social: ")
        planObraSocial = input("Plan de obra social: ")
        personas[dni] = [nombre, apellido, edad, obraSocial, planObraSocial]
        guardar_usuarios()
        print(f"Los datos de {nombre} {apellido} se guardaron con éxito.")
    input("Presione una tecla para continuar: ")
    return




def solicitarTurnos():
    ingresoSistema()
    borrar_pantalla()
    print("="*90)
    print("""Ingresó la opción [2]. Cargando lista de especialidades...




          [1] Cardiología
          [2] Médico Clínico
          [3] Pediatría
          [4] Dermatología
          [5] Psicología




          """)
    opcionTurno = input("Ingrese el número de la opción: ")




    if opcionTurno in especialidades:
        especialidad = especialidades[opcionTurno]
        borrar_pantalla()
        print("="*90)
        print(f"Eligió la opción: {opcionTurno} ({especialidad})")
        print("\nA continuación, verá los horarios disponibles. Ingrese el número del horario que desea:\n")


        for i, horario in enumerate(horarios, 1):
            if i in turnosOcupados[especialidad]:
                print(f"{i}. {horario} (Ocupado)")
            else:
                print(f"{i}. {horario}")
       
        opcionHorario = int(input("Ingrese el número del horario que desea: "))




        while opcionHorario != 0:
            if opcionHorario in turnosOcupados[especialidad]:
                print("\nEl turno seleccionado ya está ocupado. Por favor, elija otro horario.")
                break
            else:
                print(f"\nEligió la opción: {opcionHorario} ({horarios[opcionHorario - 1]})")




                dniConfirmacion = input("Confirme el turno ingresando su DNI: ")
                if dniConfirmacion in personas.keys():
                    print("\nUsted ha confirmado su turno correctamente, muchas gracias. Que tenga un buen día.")
                    turnosOcupados[especialidad].append(opcionHorario)
                    guardar_turnos()
                    break
                else:
                    print("Usted no ha confirmado el turno correctamente. Reingrese su número de DNI: ")
                    dniConfirmacion = input("Confirme el turno ingresando su DNI: ")




def eliminarTurnos():
    print("\nIngresó la opción [3]. Cargando lista de turnos...\n")
   
    if not any(turnosOcupados.values()):
        print("No hay turnos ocupados para eliminar.")
        return




    print("Especialidades:\n")
    for key, value in especialidades.items():
        print(f"{key}. {value}")




    opcionEspecialidad = input("\nIngrese el número de la especialidad del turno que desea eliminar y presione ENTER: ")




    if opcionEspecialidad in especialidades:
        especialidad = especialidades[opcionEspecialidad]
        if not turnosOcupados[especialidad]:
            print(f"No hay turnos ocupados para {especialidad}.")
            return
       
        print(f"Turnos ocupados para {especialidad}:")
        for turno in turnosOcupados[especialidad]:
            print(f"{turno}. {horarios[turno - 1]}")




        seleccionarTurno = int(input("Ingrese el número del turno que desea eliminar: "))
        if seleccionarTurno in turnosOcupados[especialidad]:
            horarioCompleto = horarios[seleccionarTurno - 1]
            confirmacion = input(f"¿Estás seguro de eliminar el turno {seleccionarTurno} ({horarioCompleto})? S/N: ")
            if confirmacion.upper() == "S":
                turnosOcupados[especialidad].remove(seleccionarTurno)
                guardar_turnos()
                print(f"Turno {seleccionarTurno} ({horarioCompleto}) eliminado correctamente.")
            else:
                print("El turno no ha sido eliminado.")
        else:
            print("El turno ingresado no existe.")




def modificarTurnos():
    print("\nEligió la opción [4]. Cargando lista de turnos...\n")


    if not any(turnosOcupados.values()):
        print("\nNo hay turnos ocupados para modificar.")
        return




    print("\nEspecialidades:\n")
    for key, value in especialidades.items():
        print(f"{key}. {value}")




    opcionEspecialidad = input("\nIngrese el número de la especialidad del turno que desea modificar y presione ENTER: ")




    if opcionEspecialidad in especialidades:
        especialidad = especialidades[opcionEspecialidad]
        if not turnosOcupados[especialidad]:
            print(f"No hay turnos ocupados para {especialidad}.")
            return
       
        print(f"Turnos ocupados para {especialidad}:")
        for turno in turnosOcupados[especialidad]:
            print(f"{turno}. {horarios[turno - 1]}")




        seleccionarTurno = int(input("Ingrese el número del turno que desea modificar: "))
        if seleccionarTurno in turnosOcupados[especialidad]:
            horarioCompleto = horarios[seleccionarTurno - 1]
            confirmacion = input(f"¿Estás seguro de modificar el turno {seleccionarTurno} ({horarioCompleto})? S/N: ")
            if confirmacion.upper() == "S":
                turnosOcupados[especialidad].remove(seleccionarTurno)
                print("Seleccione un nuevo horario:")
                for i, horario in enumerate(horarios, 1):
                    if i in turnosOcupados[especialidad]:
                        print(f"{i}. {horario} (Ocupado)")
                    else:
                        print(f"{i}. {horario}")
                opcionHorario = int(input("Ingrese el número del horario que desea: "))
                if opcionHorario not in turnosOcupados[especialidad] and 1 <= opcionHorario <= len(horarios):
                    turnosOcupados[especialidad].append(opcionHorario)
                    guardar_turnos()
                    print(f"Turno {seleccionarTurno} modificado a {opcionHorario} ({horarios[opcionHorario - 1]}) correctamente.")
                else:
                    print("El horario seleccionado ya está ocupado o no es válido.")
            else:
                print("El turno no ha sido modificado.")
        else:
            print("El turno ingresado no existe.")




def listarUsuarios():
    if not personas:
        print("No hay usuarios registrados.")
        return
   
    print("=" * 100)
    print(" Lista de Usuarios ".center(100, "-"))
    print(f"{'DNI':<15} {'Nombre':<20} {'Apellido':<20} {'Edad':<10} {'Obra Social':<15} {'Plan':<15}")
    print("-" * 100)
    for dni, datos in personas.items():
        nombre, apellido, edad, obraSocial, planObraSocial = datos
        print(f"{dni:<15} {nombre:<20} {apellido:<20} {edad:<10} {obraSocial:<15} {planObraSocial:<15}")
    print("-" * 100)
    input("Presione una tecla para continuar...")




def modificarUsuario():
    print("\nEligió la opción [6]. Cargando lista de usuarios...\n")
    dni = input("Ingrese el DNI del usuario que desea modificar: ")
    if dni in personas:
        print("\nSeleccione el campo que desea modificar:\n")
        print("[1] Nombre")
        print("[2] Apellido")
        print("[3] Edad")
        print("[4] Obra social")
        print("[5] Plan de obra social")
        print("[0] Cancelar")
       
        campo = input("\nIngrese el número del campo que desea modificar y presione ENTER: ")
        if campo == "1":
            nuevo_valor = input("Ingrese el nuevo nombre: ")
            personas[dni][0] = nuevo_valor
        elif campo == "2":
            nuevo_valor = input("Ingrese el nuevo apellido: ")
            personas[dni][1] = nuevo_valor
        elif campo == "3":
            nuevo_valor = int(input("Ingrese la nueva edad: "))
            personas[dni][2] = nuevo_valor
        elif campo == "4":
            nuevo_valor = input("Ingrese la nueva obra social: ")
            personas[dni][3] = nuevo_valor
        elif campo == "5":
            nuevo_valor = input("Ingrese el nuevo plan de obra social: ")
            personas[dni][4] = nuevo_valor
        elif campo == "0":
            print("Modificación cancelada.")
            return
        else:
            print("Opción inválida.")
            return
       
        guardar_usuarios()
        print("Datos modificados correctamente.")
    else:
        print("DNI no encontrado.")
    input("Presione una tecla para continuar...")




def menu():
    while True:
        borrar_pantalla()
        encabezado = "Clínica Médica 'Medinet'"
        print(encabezado.center(90,"="))
        print("""
        ¡Bienvenido al sistema de Atención al Cliente de la Clínica Medinet!
        A continuación, le pediremos que ingrese sus datos para una mejor atención.
        """)
        print("="*90)
        print("[1] Ingresar al sistema")
        print("[2] Seleccionar turno")
        print("[3] Eliminar turnos asignados")
        print("[4] Modificar turnos asignados")
        print("[5] Listar usuarios")
        print("[6] Modificar usuario")
        print("[0] Salir")
        print()
        laOpcion = input("Ingrese el número de la opción y presione ENTER: ")
        match laOpcion:
            case "1":
                borrar_pantalla()
                print("="*90)
                ingresoSistema()
            case "2":
                borrar_pantalla()
                print("="*90)
                solicitarTurnos()
            case "3":
                borrar_pantalla()
                print("="*90)
                eliminarTurnos()
            case "4":
                borrar_pantalla()
                print("="*90)
                modificarTurnos()
            case "5":
                borrar_pantalla()
                listarUsuarios()
            case "6":
                borrar_pantalla()
                print("="*90)
                modificarUsuario()
            case "0":
                borrar_pantalla()
                print("="*90)
                print("Eligió cerrar el programa...")
                feet = "Gracias por utilizar nuestros servicios. ¡Hasta luego!"
                print(feet.center(90,"="))
                break
            case _:
                print("Opción inexistente\n")
        input("Presione una tecla para continuar...")


menu()
