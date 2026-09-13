def calcular_salario(horas, pago_hora):
    salario = horas * pago_hora
    return salario


if __name__ == "__main__":
    horas = 40
    pago_hora = 5

    resultado = calcular_salario(horas, pago_hora)

    print("El salario semanal es:", resultado)