EI = 0
EF1 = 0
EF2 = 0
EM = 0
print("Pesquisa sobre o nível escolar")
print()

while True:
    print("Níveis escolares: ")
    print("EI - Educação infantil")
    print("EF1 - Ensino Fundamental 1")
    print("EF2 - Ensino Fundamental 2")
    print("EM - Ensino Médio")
    print("S - Sair do programa")
    opcao = input("digite a sigla da opção: ").upper()
    if opcao == "S":
        print("fim do programa")
        break

    nome = input("digite o nome do estudante: ")
    print("************************")
    if opcao == "EI":
        EI += 1
    if opcao == "EF1":
        EF1 += 1
    if opcao == "EF2":
        EF2 += 1
    if opcao == "EM":
        EM += 1

print("total de alunos na educação infantil: ", EI)
print("total de alunos no ensino fundamental 1: ", EF1)
print("total de alunos no ensino fundamental 2: ", EF2)
print("total de alunos no ensino médio: ",EM)
