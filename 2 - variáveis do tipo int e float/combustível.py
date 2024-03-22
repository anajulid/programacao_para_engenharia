#pergunta ao usuário quanto de dinheiro ele pretende usar com combustível
dinheiro = float(input("quanto de dinheiro você pretende gastar com combustível?" ))

#calcula quantos km o carro consegue rodar, considerando que a gasolina custe 4,95 e o carro ande 20 km/l
km = (dinheiro / 4.95) * 20

print ("a quantidade de km que seu carro consegue rodar com essa quantidade de combustível é:" ,km)
