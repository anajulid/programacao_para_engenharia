produtos = {}

for i in range(5):
    nome = input("insira o nome do produto: ")
    preco = float(input("digite o preço do produto: "))
    produtos.update({nome:preco})

print("lista de produtos: ", produtos)
