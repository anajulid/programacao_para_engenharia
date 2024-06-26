funcionarios = {}

while True:
    codigo = int(input("digite o código do funcionário: "))
    nome = input("digite o nome do funcionário: ")
    funcionarios [codigo] = nome

    opcao = input("deseja continuar fazendo o cadastro? S - SIM ou N - NÃO: ").upper()
    if opcao == "N":
        break

print("lista de funcionários: ",funcionarios)

demitir = int(input("informe qual funcionário deseja excluir digitando o código: "))
funcionarios.pop(demitir)

print("lista de funcionários atualizada: ", funcionarios)
