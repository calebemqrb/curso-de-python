carrinho = []

while True:
    try:
        opcao = int(input("\nEscolha uma opção: \n" 
        "1 - Inserir produto \n" 
        "2 - Apagar produto \n"
        "3 - Listar produtos\n" \
        "4 - Sair do carrinho\n\n"))

        if opcao == 4:
            break

        if opcao > 4 or opcao < 1:
            print("\nEscolha uma opção válida!\n")

        if opcao == 1:
            produto_a_inserir = str(input("\nDigite o nome do produto que deseja inserir:\n"))
            for produto in carrinho:
                if produto == produto_a_inserir:
                    print('\nO produto já esta no carrinho\n')
                    break
            carrinho.append(produto_a_inserir.lower())

        if opcao == 2:

            opcao_apagar_produto = int(input("\nDe qual forma deseja apagar o produto?\n" \
            "1 - Pelo indice\n" \
            "2 - Pelo nome\n"))

            if opcao_apagar_produto == 1:
                indice_produto_a_apagar = int(input("\nDigite o indice do produto que deseja apagar:\n"))
                for i, _ in enumerate(carrinho):
                    if i == indice_produto_a_apagar:
                        carrinho.remove(carrinho[i])
                        break
            elif opcao_apagar_produto == 2:
                nome_produto_a_apagar = input("\nDigite o nome do produto que deseja apagar:\n")
                for produto in carrinho:
                    if produto == nome_produto_a_apagar.lower():
                        carrinho.remove(produto)
                        break

        if opcao == 3:
            if carrinho == []:
                print('\nO carrinho esta vazio\n')
            else:
                for produtos in enumerate(carrinho):
                    print(produtos)
            
    except:
        print('Insira um valor válido')