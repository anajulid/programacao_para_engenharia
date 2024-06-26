n = int(input("digite a quantidade de números: "))
soma = 0

for contador in range(n):
    num = float(input("digite um número: "))
    soma += num

media = soma / n
print("média =  {:.2f}".format(media))