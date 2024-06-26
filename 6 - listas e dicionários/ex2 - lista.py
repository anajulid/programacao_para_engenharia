amigos = []

while True:
    nomes = input("insira o nome de um amigo: ")
    amigos.append(nomes)
    opcao = input("deseja inserir mais um nome? S - SIM ou N - NÃO: ").upper()
    if opcao == "N":
        break

print("\nLista de amigos:")
for amigo in amigos:
    print(amigo)