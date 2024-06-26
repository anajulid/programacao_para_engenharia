lista = []

for contador in range(1, 11):
    idade = int(input("digite sua idade: "))
    lista.append(idade)
    lista.sort(reverse=False)

print(lista)