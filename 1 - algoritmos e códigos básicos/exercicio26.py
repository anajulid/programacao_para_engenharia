#calcula qual valor tem que ser investido pra se obter valor x ao fim daquele investimento

fv = float(input("Qual valor você deseja no fim do investimento? "))
n = int(input("Por quantos meses você pretende investir? "))
i = float(input("Qual é a rentabilidade mensal desse investimento? "))

i = i / 100

v_inicial = fv / (1 + i)**n

print ("Valor inicial a ser investido: ",v_inicial)