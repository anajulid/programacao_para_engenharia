#10

n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))

media = (n1 + n2 + n3)/3
print (f"A média é de R$ {media:,.2f}")

if media >= 7:
    print ("parabéns! sua média é alta.")
elif media >= 5 and media < 7:
    print ("sua média é razoável.")
else:
    print ("sua média é baixa. é uma boa oportunidade para melhorar")



