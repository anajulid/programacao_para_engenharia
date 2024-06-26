def somar_numeros(x):
    soma = 0
    for i in range (0, x+1):
        #acumulador
        soma = soma + i
    print("soma dos números menores/iguais a ",x," = ", soma)
    return

#principal
numero = int(input("digite um número: "))
somar_numeros(numero)
