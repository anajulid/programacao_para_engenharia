def calcular_media(a,b,c):
    media = (a + b + c)/3
    return media

def verificar_situacao(resul):
    if resul >= 6:
        print("aluno aprovado")
    elif 4 <= resul <= 6:
        print("verificação suplementar")
    else:
        print("aluno reprovado")

while True:
    nome = input("Digite nome do aluno:  ")
    nota1 = float(input("digite a primeira nota: "))
    nota2 = float(input("digite a segunda nota: "))
    nota3 = float(input("digite a terceira nota: "))
    
    resultado = calcular_media(nota1,nota2,nota3)
    print("aluno: ", nome, "- média final: ", resultado)

    verificar_situacao(resultado)
    
    opcao = input("deseja continuar? S - SIM ou N - NÃO ").upper()
    if opcao == "N":
        break
