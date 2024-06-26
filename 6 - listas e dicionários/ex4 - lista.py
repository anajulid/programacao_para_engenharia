pares = []
impares = []

for contador in range (1, 6):
    numeros = int(input("digite um número: "))

    if numeros % 2 == 0:
        pares.append (numeros)
    else:
        impares.append (numeros)

print("números pares: ", pares)
print("númeoros ímpares: ", impares)
