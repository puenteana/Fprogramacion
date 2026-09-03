print("Bienvenido al sistema de reserva de asientos del cine.")

# Asientos representados como una matriz (0 = disponible, 1 = reservado)
asientos = [[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]]

fila = int(input("Ingrese la fila (0-2): "))
columna = int(input("Ingrese la columna (0-3): "))

if asientos[fila][columna] == 0:
    print("El asiento está disponible.")
    respuesta = input("¿Desea reservar el asiento? (si/no): ")
    if respuesta.lower() == "si":
        print("Reservando el asiento...")
        asientos[fila][columna] = 1
        print("El asiento ha sido reservado exitosamente.")
    else:
        print("No se ha reservado el asiento.")
    
else:
    print("El asiento no está disponible.")

# Mostrar el estado actual de los asientos
for i in range(len(asientos)):
    for j in range(len(asientos[i])):
        print(asientos[i][j], end=" ")
    print()



