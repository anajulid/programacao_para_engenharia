nome = input("nome do funcionário: ")
horas = int(input("número de horas trabalhadas: "))
valor_hora = float(input("valor da hora trabalhada: "))

salario_bruto = horas * valor_hora
salario_liq = salario_bruto - (salario_bruto * 2/100)

print ("nome do funcionário: ",nome)
print ("salário líquido: ",salario_liq)