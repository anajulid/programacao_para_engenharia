produtos = {}

n = int(input("quantos produtos deseja cadastrar? "))

for i in range(n):
    nome = input("digite o nome do produto: ")
    preco = float(input("digite o preço do produto: "))
    produtos.update({nome:preco})

print("lista de produtos: ", produtos)

remover = input("qual produto deseja excluir? ")
produtos.pop(remover)

print("lista de produtos atualizada", produtos)
