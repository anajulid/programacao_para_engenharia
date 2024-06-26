a = []
b = []
c = []

for _ in range(5):
    valor1 = int(input("Digite um valor para a lista A: "))
    a.append(valor1)
    valor2 = int(input("Digite um valor para a lista B: "))
    b.append(valor2)
    c.append(valor1)
    c.append(valor2)
    
print("lista A: ", a)
print("lista B: ", b)
print("lista C (intercaladas A e B) : ", c)