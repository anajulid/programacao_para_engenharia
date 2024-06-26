notas = []

n = int(input("insira quantos alunos serão cadastrados: "))

for contador in range (0, n):
    valor = input("insira uma nota: ")
    notas.append(valor)

print()
print("número de alunos: ", n)
print("lista de notas digitadas: ",notas)