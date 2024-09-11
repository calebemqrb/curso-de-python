while True:
    try:
        escolha = int(input(
            "Escolha uma opção: \n"
            "1 - Somar \n"
            "2 - Subtratir \n"
            "3 - Multiplicar \n"
            "4 - Dividir \n"
            "5 - Sair \n"
            ))
        
        if escolha == 5:
            break

        if escolha > 5 or escolha < 1:
            print("\nEscolha uma opção válida!\n")
        
        primeiro_nmr = float(input("\nDigite um número: "))
        segundo_nmr = float(input("Digite outro número: "))

        if escolha == 1:
            print(f'\nResultado: {primeiro_nmr + segundo_nmr}\n')
        elif escolha == 2:
            print(f'\nResultado: {primeiro_nmr - segundo_nmr}\n')
        elif escolha == 3:
            print(f'\nResultado: {primeiro_nmr * segundo_nmr}\n')
        elif escolha == 4:
            print(f'\nResultado: {primeiro_nmr / segundo_nmr}\n')

    except:
        print("\nInsira um valor válido \n")
