notas = []

for contador in range (1, 11):
    nome = input("digite o nome do aluno: ")
    soma = 0

    for contador in range(0, 2):
        nota = float(input("digite uma nota: "))
        notas.append(nota)
        soma = soma + nota

    print("nome do aluno: ", nome)
    media = (soma / 2)
    print(media)
    print()


