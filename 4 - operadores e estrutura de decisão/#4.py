#4

letra = input("digite uma letra qualquer: ").upper()

match letra:
    case "A"|"E"|"I"|"O"|"U":
        print ("a letra é uma vogal")
    case _:
        print ("a letra é uma consoante")

        
