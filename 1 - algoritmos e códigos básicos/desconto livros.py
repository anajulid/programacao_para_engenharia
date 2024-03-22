x = int(input("número de cópias do livro: "))
preco = 24.95 - ((35 / 100) * 24.95)
preco_desc = preco * x
transporte = 3 * 1 + 0.75 * (x - 1) 
custo_total = preco_desc + transporte
print ("custo total de atacado para essa quantidade de cópias: ",custo_total)