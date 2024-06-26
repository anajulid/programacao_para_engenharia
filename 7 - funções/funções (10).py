def calcular(a, b):
    media = (a + b)/2
    return media

while True:
    nome = input("nome do aluno: ")
    nota1 = float(input("digite a primeira nota: "))
    nota2 = float(input("digite a segunda nota: "))
    #chamada da função
    resultado = calcular(nota1, nota2)
    print("média final: ", resultado)

    opcao = input("deseja continuar? S - SIM ou N - NÃO ").upper()
    if opcao == "N":
        break
