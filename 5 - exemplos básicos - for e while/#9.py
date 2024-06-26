nome = input("digite seu nome: ")

nota = float(input("digite sua nota: "))

while nota < 0 or nota > 10:
    print("valor inválido!")
    nota = float(input("digite sua nota novamente: "))

print(f"O(A) aluno(a) {nome} obteve a nota {nota}.")
