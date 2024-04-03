torque = float(input("digite o valor do torque aplicado em Nm: "))
torque_rec = float(input("digite o valor do torque recomendado em Nm para o parafuso usado: "))

if torque == 1.1 * torque_rec or torque_rec * 0.9:
    print("o parafuso está apertado corretamente")
else:
    print("o parafuso não está apertado corretamente")
