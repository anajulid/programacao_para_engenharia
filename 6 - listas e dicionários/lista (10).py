medias = []
total = 0

for contador in range (0, 5):
    print(f"digite notas do aluno {contador+1}")
    n1 = float(input("insira a nota 1: "))
    n2 = float(input("insira a nota 2: "))
    n3 = float(input("insira a nota 3: "))
    n4 = float(input("insira a nota 4: "))
    media = (n1 + n2 + n3 + n4)/4
    print("média do aluno: ", media)
    medias.append(media)

    if media >= 7:
        total += 1

print("lista de medias digitadas: ", medias)
print("total de alunos aprovados: ", total)