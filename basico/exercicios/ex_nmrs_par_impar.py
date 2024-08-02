nmr = input("Insira um número:")

try:
    nmr_convertido = int(nmr)
    if nmr_convertido % 2 == 0:
        print(f"{nmr_convertido} é um número par")
    else:
        print(f"{nmr_convertido} é um número impar")

except:
    print("O valor inserido não é um numero inteiro")