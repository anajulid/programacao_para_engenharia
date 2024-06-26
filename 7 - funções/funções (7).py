def imprimir_dados(a, b, lim):
    if (a + b) > lim:
        return True
    else:
        return False

while True:
    valorA = int(input("digite o valor A: "))
    valorB = int(input("digite o valor B: "))
    limite = int(input("digite um valor limite: "))

    resultado = imprimir_dados(valorA, valorB, limite)
    print("a soma do valor A e do valor B é maior que o limite: ",resultado)

    opcao = input("deseja continuar? S - SIM ou N - NÃO").upper()
    if opcao == "N":
        break
