numero = 1
soma = 0
i = 0
maior = numero
menor = numero

while numero > 0:
    numero = int(input("digite um valor inteiro: "))

    if numero < 0:
        print("fim do programa")
        break

    if numero >= 0:
        soma += numero 
        i += 1

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

media = soma / i

print("soma dos números digitados: ",soma)
print("média dos números digitados",media)
print("maior número digitado: ",maior)
print("menor número digitado: ",menor)