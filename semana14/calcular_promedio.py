def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3)/3
    return promedio

if __name__ == "__main__":
    nota1 = 20
    nota2 = 20
    nota3 = 20

    resultado = calcular_promedio(nota1, nota2, nota3)

    print ("El promedio calculado es:", resultado)

