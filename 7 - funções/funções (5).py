def verificar_numero(x):
    if x % 2 == 0:
        print("o número digitado é par")
    else:
        print("o número digitado é ímpar")
    return

numero = int(input("digite um número qualquer: "))
verificar_numero(numero)
