lista = []
vogal = 0
consoante = 0

for contador in range(1, 6):
    carac = input("digite uma letra: ").lower()
    lista.append(carac)

    if carac == "a" or carac == "e" or carac == "i" or carac == "o" or carac == "u":
        vogal += 1
    else:
        consoante += 1

print("quantidade de vogais digitadas: ", vogal)
print("quantidade de consoantes digitadas: ", consoante)
print(lista)
    