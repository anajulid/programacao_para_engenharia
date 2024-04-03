#9

a = int(input("valor 1: "))
b = int(input("valor 2: "))
print("escolha a operação desejada: A - ADIÇÃO, S - SUBTRAÇÃO, M - MULTIPLICAÇÃO E D - DIVISÃO")

operacao = input ("digite a operação matemática desejada: ").upper()
match operacao:
    case "A":
        print ("o resultado da operação é: ", a+b)
    case "S":
        print ("o resultado da operação é ", a-b)
    case "M":
        print ("o resultado da operação é: ", a*b)
    case "D":
        print ("o resultado da operação é: ", a/b)
