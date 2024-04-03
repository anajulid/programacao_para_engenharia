litros = float(input("digite quantos litros foram vendidos: "))
comb = input("digite o tipo de combustível: A - Álcool e G - Gasolina: ").upper()

d1_alcool = 4.98 - (2/100 * 4.98)
d2_alcool = 4.98 - (5/100 * 4.98)

d1_gasol = 5.57 - (4/100 * 5.57)
d2_gasol = 5.57 - (6/100 * 5.57)

if comb == "A" and litros <= 20:
    print (f"o valor a ser pago é: {d1_alcool * litros:,.2f}")
elif comb == "A" and litros > 20:
    print (f"o valor a ser pago é: {d2_alcool * litros:,.2f}")
elif comb == "G" and litros <= 20:
    print (f"o valor a ser pago é: {d1_gasol * litros:,.2f}")
else:
    print (f"o valor a ser pago é: {d2_gasol * litros:,.2f}")