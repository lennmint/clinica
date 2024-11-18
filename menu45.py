def mostrarHorarioMatutino():
    print("El horario del turno de la mañana es de 08 a 12 horas")
def mostrarHorarioVespertino():
    print("El horario del turno de la tarde es de 14 a 18 horas")
def mostrarHorarioNocturno():
    print("El horario del turno de la noche es de 19 a 23 horas")
def mostrarMenu():
    print("Bienvenidos a la Universidad! ¿Qué horarios desea consultar?: ")
    print("1. Mañana")
    print("2. Tarde")
    print("3. Noche")
mostrarMenu()

opcion_elegida = int(input("Elige una opción (1, 2 o 3): "))
if opcion_elegida == 1:
    mostrarHorarioMatutino()
elif opcion_elegida == 2:
    mostrarHorarioVespertino()
elif opcion_elegida == 3:
    mostrarHorarioNocturno()
else:
    print("Opción no válida. Por favor, elige 1, 2 o 3.")