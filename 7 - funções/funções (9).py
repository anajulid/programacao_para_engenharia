def cadastrar(x):
    alunos = {}
    for i in range(x):
        nome = input("digite o nome do aluno: ")
        curso = input("digite o curso do aluno: ")
        alunos.update({nome:curso})
        print(alunos)
    return

n = int(input("quantos alunos deseja cadastrar? "))
cadastrar(n)
