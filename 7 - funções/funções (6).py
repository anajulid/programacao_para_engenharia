def somar(a, b):
    soma = a + b
    print("resultado: ",a, "+", b, " = ", soma)
    return soma

def subtrair(a, b):
    subtracao = a - b
    print("resultado: ",a, "-", b, " = ", subtracao)
    return subtracao

def multiplicar (a, b):
    multiplicacao = a*b
    print("resultado: ",a, "x", b, " = ", multiplicacao)
    return multiplicacao

def dividir(a, b):
    divisao = a/b
    print("resultado: ",a, "/", b, " = ", divisao)
    return divisao

while True:
    print("*******************************")
    print("Operações da Calculadora: ")
    print ("1 - adição")
    print ("2 - subtração")
    print ("3 - multiplicação")
    print ("4 - divisão")
    print ("5 - sair do programa")
    opcao = int(input("digite o número da opção desejada: "))
    
    if opcao == 5:
        print("fim do programa!")
        break

    valor1 = int(input("digite o primeiro valor: "))
    valor2 = int(input("digite o segundo valor: "))

    if opcao == 1:
        somar(valor1, valor2)
    if opcao == 2:
        subtrair(valor1, valor2)
    if opcao == 3:
        multiplicar(valor1, valor2)
    if opcao == 4:
        dividir(valor1, valor2)
