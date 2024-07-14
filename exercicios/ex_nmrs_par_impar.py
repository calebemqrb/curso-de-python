nmr = input("Insira um número:")

try:
    int(nmr)
    if nmr % 2 == 0:
        print(f"{nmr} é um número par")
    else:
        print(f"{nmr} é um número impar")

except:
    print("O valor inserido não é um numero inteiro")