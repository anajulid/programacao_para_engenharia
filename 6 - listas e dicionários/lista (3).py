lista = []
soma = 0

for contador in range (0, 4):
    notas = float(input("digite uma nota: "))
    soma += notas
    lista.append(notas)

media = soma/4
print(lista)
print("media das notas: ", media)