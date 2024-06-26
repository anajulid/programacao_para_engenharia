estoque = {}
n = int(input("Quantos produtos deseja cadastrar: "))

for i in range(n):
    codigo = int(input("Digite codigo produto: "))
    nome = input("digite nome produto: ")
    estoque[codigo] = nome

print ("Lista de produtos cadastrados:", estoque)
