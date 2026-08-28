matriz = [[0 for i in range(5)] for j in range(5)]
for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input(f"Digite un valor para la posición [{i}][{j}]: "))
print("Matriz ingresada:")
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end=" ")
    print()
    