nome = "Nome Qualquer"
i = 0
novo_nome = ''

while i < len(nome):
    novo_nome += f'*{nome[i]}'
    i += 1

novo_nome += '*'

print(novo_nome)