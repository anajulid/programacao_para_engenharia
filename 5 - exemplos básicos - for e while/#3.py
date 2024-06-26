numero = int(input("digite o 1º número: "))

maior = numero
menor = numero

for contador in range(1, 10):

    numero = int(input("digite número: "))

    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

print("maior número digitado: ", maior)
print("menor número digitado: ", menor)