#calcula qual o valor do montante se for investido um valor x durante y meses a uma taxa qualquer

pv = float(input("valor inicial do investimento: "))
n = int(input("número de meses de aplicação: "))
i = float(input("rentabilidade mensal do investimento: "))
i = i/100
fv = pv*(1+i)**n
print (fv)
