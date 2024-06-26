def verificar_numero(x):
    if x < 0:
        print("o número é negativo")
    elif x > 0:
        print("o número é positivo")
    else:
        print("o número digitado é 0")
    return

numero = int(input("digite um número qualquer: "))
verificar_numero(numero)
