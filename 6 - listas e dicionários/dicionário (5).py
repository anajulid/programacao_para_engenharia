agenda = {}

n = int(input("quantos nomes deseja cadastrar: "))

for i in range(n):
    nome = input("digite seu nome: ")
    telefone = input("digite seu telefone: ")
    #criar uma lista dentro do dicionário
    agenda.update({nome:telefone})

print("agenda telefônica com nome e telefone: ", agenda)

nome = input("digite um novo nome: ")
telefone = input("digite um novo telefone: ")
agenda.update({nome:telefone})

print("agenda atualizada: ",agenda)