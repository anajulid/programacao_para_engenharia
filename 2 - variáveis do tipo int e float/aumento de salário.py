#calcula qual seria o salário final de um funcionário se ele recebesse um aumento de 5%

nome = input("nome do funcionário: ")
cargo = input("cargo do funcionário: ")
salario = float(input("salário do funcionário: "))
salario_aumen = salario + (salario * (5/100))

print ("nome do funcionário:",nome,",cargo do funcionário: ",cargo,"salário atual do funcionário: ",salario,"salário com aumento de 5%: ",salario_aumen)
