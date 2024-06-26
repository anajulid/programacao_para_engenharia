maiores = 0
menores = 0

for contador in range(1, 11):
    nome = input("digite seu nome: ")
    idade = int(input("digite sua idade: "))
    print("*******************************")

    if idade >= 18:
        maiores += 1
    else:
        menores += 1
    
print("a quantidade de pessoas maiores de idade cadastradas é: ",maiores)
print("a quantidade de pessoas menores de idade cadastradas é: ",menores)