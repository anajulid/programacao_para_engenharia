DB = 0
HP = 0
CO = 0
AS = 0
NP = 0
homens = 0
mulheres = 0

while True:
    print("Tipo da doença: ")
    print("DB - Diabetes")
    print("HP - Hipertensão")
    print("CO - Colesterol alto")
    print("AS - Asma")
    print("NP - Não possui doença")
    print("X - Encerrar pesquisa")
    opcao = input("digite a sigla da opção: ").upper()

    if opcao == "X":
        print()
        print("PESQUISA ENCERRADA")
        print()
        break

    nome = input("digite seu nome: ")

    sexo = input("digite seu sexo (M ou F): ").upper()
    print("**********************")
    if sexo == "M":
        homens += 1
    elif sexo == "F":
        mulheres += 1

    if opcao == "DB":
        DB += 1
    if opcao == "HP":
        HP += 1
    if opcao == "CO":
        CO += 1
    if opcao == "AS":
        AS += 1
    if opcao == "NP":
        NP += 1

print("total de pessoas com diabetes: ", DB)
print("total de pessoas com hipertensão: ", HP)
print("total de pessoas com colesterol alto: ", CO)
print("total de pessoas com asma: ", AS)
print("total de pessoas que não possuem doenças: ", NP)
print()
print("total de homens: ", homens)
print("total de mulheres: ", mulheres)    