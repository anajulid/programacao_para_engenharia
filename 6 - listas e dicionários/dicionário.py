d = {}

n = int(input("quantos nomes deseja cadastrar: "))

for i in range(n):
    nome = input("digite seu nome: ")
    idade = int(input("digite sua idade: "))
    sexo = input("digite seu sexo: M - Masculino ou F - Feminino: ").upper()
    #criar uma lista dentro do dicionário
    contato = []
    contato.append(idade)
    contato.append(sexo)
    d.update({nome:contato})

print("lista de contatos: ", d)
