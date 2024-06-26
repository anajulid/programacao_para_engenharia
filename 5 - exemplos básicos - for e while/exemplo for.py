soma = 0

for contador in range(1,6):
    numero = int(input("digite um número: "))
    soma += numero

print("soma dos números digitados: ", soma)
print("média dos números digitados: ", soma / contador)
