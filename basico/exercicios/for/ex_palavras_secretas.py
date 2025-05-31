import os

palavra_secreta = 'Teste'
letras_acertadas = ''
qtd_tentativas = 0

while True:

    letra_escolhida = str(input("Escolha uma letra:\n")).lower()

    if len(letra_escolhida) > 1:
        print("Escolha uma letra por vez")
        continue

    if letra_escolhida in palavra_secreta:
        letras_acertadas += letra_escolhida

    palavra_secreta_formada = ''
    for letra_secreta in palavra_secreta.lower():
        if letra_secreta in letras_acertadas:
            palavra_secreta_formada += letra_secreta
        else:
            palavra_secreta_formada += '*'

    print(palavra_secreta_formada)
    qtd_tentativas += 1

    if palavra_secreta.lower() == palavra_secreta_formada:
        os.system('cls')
        print(f'Parabéns, você adivinhou a palavra!\nA palavra secreta era: {palavra_secreta}\nTentaivas: {qtd_tentativas}')
        break