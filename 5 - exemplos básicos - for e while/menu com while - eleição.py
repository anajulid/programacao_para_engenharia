cand1 = 0   # inicia a contagem dos votos a partir de 0
cand2 = 0
cand3 = 0 
cand4 = 0
nulo = 0
branco = 0

while True: # enquanto não for dado o comando para encerrar o programa
    print("Códigos dos candidatos: ") #menu dos códigos dos candidatos
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
    
    #contagem dos votos
    if opcao == "1":
        cand1 += 1
    elif opcao == "2":
        cand2 += 1
    elif opcao == "3":
        cand3 += 1
    elif opcao == "4":
        cand4 += 1
    elif opcao == "5":
        nulo += 1
    elif opcao == "6":
        branco += 1

print("O candidato 1 - João recebeu",cand1,"votos.")
print("O candidato 2 - Pedro recebeu",cand2,"votos.")
print("O candidato 3 - José recebeu",cand3,"votos.")
print("O candidato 4 - Paulo recebeu",cand4,"votos.")
print("Um total de ",nulo,"votos foram nulos.")
print("Um total de ",branco,"votos foram brancos.")
print("***********************")

# faz a verificação de qual candidato recebeu mais votos e indica o vencedor
vencedor = 1
max_votos = cand1

if cand2 > max_votos:
    vencedor = 2
    max_votos = cand2

if cand3 > max_votos:
    vencedor = 3
    max_votos = cand3

if cand4 > max_votos:
    vencedor = 4
    max_votos = cand4

if vencedor == 1:
    print("O ganhador da eleição foi o candidato 1 - João.")
elif vencedor == 2:
    print("O ganhador da eleição foi o candidato 2 - Pedro.")
elif vencedor == 3:
    print("O ganhador da eleição foi o candidato 3 - José.")
elif vencedor == 4:
    print("O ganhador da eleição foi o candidato 4 - Paulo.")
