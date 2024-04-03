#3

nome = input("digite seu nome: ")
sexo = input("digite seu sexo em letras M ou F: ").upper()

match sexo:
    case "M":
        print ("sexo masculino")
    case "F":
        print ("sexo feminino")
    case _:
        print ("sexo não informado")
        
