horario = input("Insira o horário:")

try:
    horario_convertido = int(horario)
    if horario_convertido >=0 and horario_convertido <= 11:
        print("Bom dia")
    elif horario_convertido >=12 and horario_convertido <= 17:
        print("Boa tarde")
    elif horario_convertido >=18 and horario_convertido <= 23:
        print("Boa noite")
    else:
        raise

except:
    print("Valor invalido")