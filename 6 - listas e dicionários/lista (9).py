lista = []

for contador in range(1, 6):
    numero = int(input("digite um número: "))
    lista.append(numero)

print("maior número da lista: ", max(lista))
print("menor número da lista: ", min(lista))