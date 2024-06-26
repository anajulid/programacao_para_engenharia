nome = input("digite seu nome: ")
salario = float(input("digite seu salário: "))
estado_civil = input("digite seu estado civil: S - SOLTEIRO, C - CASADO, V - VIÚVO, D - DIVORCIADO: ").upper()
idade = int(input("digite sua idade: "))
sexo = input("digite seu sexo: F - FEMININO, M - MASCULINO: ").upper()

while len(nome) < 3:
    nome = input("digite seu nome novamente: ")
while salario < 0:
    salario = float(input("digite seu salário novamente: "))
while idade < 0 or idade > 100:
    idade = int(input("digite sua idade: "))