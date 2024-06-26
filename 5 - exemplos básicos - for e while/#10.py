nome = input("digite seu nome: ")
senha = input("digite uma senha: ")

while senha == nome:
    print("senha inválida!")
    nota = float(input("digite sua senha novamente: "))

print("o cadastro foi realizado com sucesso.")
