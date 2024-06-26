numero = int(input("digite um número: "))
i = 1

for contador in range (1, numero+1):
    i = i * contador 
    contador += 1

print(f"o fatorial de {numero} = ", i)