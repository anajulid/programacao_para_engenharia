nome = input("digite seu nome: ")
print ("estado civil: C - CASADO ou S - SOLTEIRO ou V - VIÚVO")

#coloca o upper no final pra independente de se o usuário colocar maiúscula ou minúscula, rodar
estado = input("digite seu estado civil: ").upper()
match estado:
    case "C":
        print ("estado civil: casado")
    case "S":
        print ("estado civil: solteiro")
    case "V":
        print ("estado civil: viúvo")
    case _:
        print ("estado civil não informado")
