cand1 = 0
cand2 = 0
cand3 = 0 
cand4 = 0
nulo = 0
branco = 0

while True:
    print("Códigos dos candidatos: ")
    print("1 - João")
    print("2 - Pedro")
    print("3 - José")
    print("4 - Paulo")
    print("5 - Voto Nulo")
    print("6 - Voto em branco")
    print("X - Encerrar votação")
    opcao = input("Digite o código: ").upper()
    print("*************************")

    if opcao == "X":
        print()
        print("VOTAÇÃO ENCERRADA")
        print()
        break
    
    if opcao == "1":
        cand1 += 1
    if opcao == "2":
        cand2 += 1
    if opcao == "3":
        cand3 += 1
    if opcao == "4":
        cand4 += 1
    if opcao == "5":
        nulo += 1
    if opcao == "6":
        branco += 1

print("***********************")
print("O candidato 1 - João recebeu",cand1,"votos.")
print("O candidato 2 - Pedro recebeu",cand2,"votos.")
print("O candidato 3 - José recebeu",cand3,"votos.")
print("O candidato 4 - Paulo recebeu",cand4,"votos.")
print("Um total de ",nulo,"votos foram nulos.")
print("Um total de ",branco,"votos foram brancos.")
print("***********************")
