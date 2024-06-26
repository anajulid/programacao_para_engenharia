homens = 0
mulheres = 0

for contador in range(1, 6):
    nome = input("digite seu nome: ")

    sexo = input("digite seu sexo (M ou F): ").upper()
    if sexo == "M":
        homens += 1
    elif sexo == "F":
        mulheres += 1

    altura = float(input("digite sua altura: "))
    if sexo == "M":
        peso_ideal = ((72.7 * altura) - 58)
        print("seu peso ideal é: ", peso_ideal)
    elif sexo == "F":
        peso_ideal = ((62.1 * altura) - 44.7)
        print("seu peso ideal é: ", peso_ideal)

    print("*******************************")

    
print("a quantidade de homens é: ",homens)
print("a quantidade de mulheres é: ",mulheres)