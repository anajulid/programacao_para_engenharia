n1 = int(input("digite um número: "))
n2 = int(input("digite um número: "))
soma = 0

for contador in range(n1, n2 + 1):
    print(contador)
    soma += contador
    
print("a soma dos números é: ",soma)