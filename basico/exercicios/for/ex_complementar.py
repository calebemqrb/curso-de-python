json = [{'nome': 'calebe', 'idade': 21},{'nome': 'calebe', 'idade': 21},{'nome': 'teste', 'idade': 15}]

nomes_lidos = []
json_filtrado = []
qtd_aparicoes_nome = {}

for pessoa in json:
    nome = pessoa['nome']
    if nome not in nomes_lidos:
        nomes_lidos.append(nome)
        json_filtrado.append(pessoa)

    if nome in qtd_aparicoes_nome:
        qtd_aparicoes_nome[nome] += 1
    else:
        qtd_aparicoes_nome[nome] = 1

resultado = []
for nome in qtd_aparicoes_nome:
    resultado.append({'nome': nome, 'qtd_aparições': qtd_aparicoes_nome[nome]})

print(json_filtrado)
print(resultado)