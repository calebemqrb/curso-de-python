frase = 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. \
    Mollitia illum veritatis velit accusamus vero. Omnis sunt, ullam \
    recusandae eos harum aliquid fugiat, ipsa, modi sint quaerat sequi\
    dicta eum incidunt.Illum amet quia ab unde cupiditate quae magni\
    non nihil saepe quisquam sunt quod ad facere recusandae numquam rerum\
    dolore fugiat beatae cum quo distinctio ea nemo in. At.'

i = 0
maior_qtd_aparicoes = 0
letra_apereceu_mais = ''
while i< len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i +=1
        continue

    qtd_aparicoes_letra_atual= frase.count(letra_atual)

    if maior_qtd_aparicoes < qtd_aparicoes_letra_atual:
        maior_qtd_aparicoes = qtd_aparicoes_letra_atual
        letra_apereceu_mais = letra_atual
 
    i+=1

print(f'Letra que apareceu mais vezes: {letra_apereceu_mais}\
      \n Qtd de aparições: {maior_qtd_aparicoes}')