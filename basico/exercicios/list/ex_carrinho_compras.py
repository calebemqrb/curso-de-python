carrinho = []

while True:
    try:
        opcao = int(input("Escolha uma opção: \n" 
        "1 - Inserir produto \n" 
        "2 - Apagar produto \n"
        "3 - Listar produtos\n" \
        "4 - Sair do carrinho\n\n"))

        if opcao == 4:
            break

        if opcao > 4 or opcao < 1:
            print("\nEscolha uma opção válida!\n")

        if opcao == 1:
            produto_a_inserir = str(input("Digite o nome do produto que deseja inserir:\n"))
            for produto in carrinho:
                if produto == produto_a_inserir:
                    print('O produto já esta no carrinho')
                    break
            carrinho.append(produto_a_inserir.lower())

        if opcao == 2:

            #Corrigir essa opção
            #Falha ao tentar apagar passando indice do produto
            #Problema: o input transforma os dados recebidos em str
            #Solução pensada: outro input: int(input)

            produto_a_apagar = input("Digite o indice ou nome do produto que deseja apagar:\n")
            print(type(produto_a_apagar))
            if type(produto_a_apagar) == str:
                for produto in carrinho:
                    if produto == produto_a_apagar.lower():
                        carrinho.remove(produto)
                        break
            elif type(produto_a_apagar) == int:
                for i in len(carrinho):
                    if i == produto_a_apagar:
                        print(i, produto_a_apagar)
                        carrinho.remove(carrinho[i])
                        break

            else:
                print('Tipo de dado invalido')

        if opcao == 3:
            if carrinho == []:
                print('O carrinho esta vazio')
            else:
                for produtos in enumerate(carrinho):
                    print(produtos)
            
    except:
        print('Insira um valor válido')