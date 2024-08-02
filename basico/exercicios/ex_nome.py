nome = input("Insira seu primeiro nome:")

try:
    nome_convertido = str(nome)
    tamanho_nome = len(nome_convertido)
    if tamanho_nome <= 4:
        print("Nome curto")
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
except:
    print("Valor invalido")