lista = []
pares = []
impares = []

for contador in range (1, 6):
    numeros = int(input("digite um número: "))
    lista.append(numeros)

    if numeros % 2 == 0:
        pares.append (numeros)
    else:
        impares.append (numeros)

print("todos os números digitados: ", lista)
print("números pares: ", pares)
print("númeoros ímpares: ", impares)