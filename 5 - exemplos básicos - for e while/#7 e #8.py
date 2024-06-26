pares = []
impares = []

print("digite 10 números inteiros positivos: ")

for contador in range(1, 11):

    numero = int(input("digite número: "))

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("números pares: ", pares)
print("números ímpares: ", impares)