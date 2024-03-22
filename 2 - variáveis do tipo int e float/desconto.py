#calcula o preço final de um produto considerando que ele tenha 20% de desconto

preco = float(input("preço original do produto: "))
desconto = preco * 20/100
preco_desc = preco - (preco * 20/100)

print("preço original do produto: ",preco)
print("você recebeu R$",desconto,"de desconto")
print("preço do produto com desconto: ",preco_desc)
