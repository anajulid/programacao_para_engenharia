#12

v = int(input("insira o valor da tensão em volts: "))
i = int(input("insira o valor da corrente em amperes: "))
r = int(input("insira o valor da resistência em ohms: "))

tensao_esp = i * r

if tensao_esp == v:
    print ("O componente obedece à Lei de Ohm.")
else:
    print ("O componente não obedece à Lei de Ohm.")

