positivos = 0
negativos = 0

for contador in range(1, 6):
    numero = int(input("digite um número: "))

    if numero < 0:
        negativos += 1
    if numero >= 0:
        positivos += 1

print("quantidade de números positivos: ", positivos)
print("quantidade de números negativos: ", negativos)
