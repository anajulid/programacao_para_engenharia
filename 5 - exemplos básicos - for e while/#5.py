numero = int(input("digite o 1º número: "))

maior = numero
menor = numero 

for contador in range(1, 10):
    numero = int(input("digite mais um número: "))

    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("o maior número é: ", maior)
print("o menor número é: ", menor)