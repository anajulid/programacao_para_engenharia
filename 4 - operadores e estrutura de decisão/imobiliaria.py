nome = input("digite seu nome: ")
imoveis = int(input("digite a quantidade de imóveis vendidos: "))
venda = float(input("digite o valor total de vendas: "))

salario = 1500 + (200*imoveis) + (0.05*(venda/imoveis))

print(nome, "seu salário final será de: ",salario)

