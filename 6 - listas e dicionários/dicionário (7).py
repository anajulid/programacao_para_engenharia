notas = {}

while True:
    nome = input("insira o nome do aluno: ")
    medias = []
    
    nota1 = float(input("insira a nota 1: "))
    nota2 = float(input("insira a nota 2: "))
    nota3 = float(input("insira a nota 3: "))
    media = (nota1 + nota2 + nota3)/3
        
    if media >= 7:
        situacao = "aprovado"
    elif 5 <= media <= 7:
        situacao = "aluno em recuperação"
    else:
        situacao = "reprovado"
        
    medias.append("%.2f"% media)
    medias.append(situacao)
    notas.update({nome:medias})

    opcao = input("deseja continuar? S - SIM ou N - NÃO ").upper()
    if opcao == "N":
        break

print(notas)
