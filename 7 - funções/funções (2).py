def cadastro(x):
    funcionarios = {}
    for i in range(x):
        nome = input("digite o nome do funcionário: ")
        salario = float(input("digite o salário do funcionário: "))
        if salario == 0:
            salario = 9000
        funcionarios.update({nome:salario})
    print(funcionarios)
    return

n = int(input("insira quantos funcionários deseja cadastrar: "))
cadastro(n)
