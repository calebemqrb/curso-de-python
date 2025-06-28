cpf = '746.824.890-70'
cpf_filtrado = cpf.replace('.', '').replace('-', '')
nove_primeiros_digitos_do_cpf = cpf_filtrado[:9]
soma_dos_digitos_multiplicados = 0
contador = 10
for digito in nove_primeiros_digitos_do_cpf:
    soma_dos_digitos_multiplicados += int(digito) * contador
    contador -= 1

soma_dos_digitos_multiplicados = soma_dos_digitos_multiplicados * 10
novo_digito_gerado = soma_dos_digitos_multiplicados % 11
novo_digito_gerado = 0 if novo_digito_gerado > 9 else novo_digito_gerado

dez_primeiros_digitos_do_cpf = nove_primeiros_digitos_do_cpf + str(novo_digito_gerado)
contador = 11
soma_dos_digitos_multiplicados = 0
for digito in dez_primeiros_digitos_do_cpf:
    soma_dos_digitos_multiplicados += int(digito) * contador
    contador -= 1

soma_dos_digitos_multiplicados = soma_dos_digitos_multiplicados * 10
novo_digito_gerado = soma_dos_digitos_multiplicados % 11
novo_digito_gerado = 0 if novo_digito_gerado > 9 else novo_digito_gerado
cpf_encontrado = dez_primeiros_digitos_do_cpf + str(novo_digito_gerado)

cpf_encontrado_formatado = cpf_encontrado[:3] + '.' + cpf_encontrado[3:]
cpf_encontrado_formatado = cpf_encontrado_formatado[:7] + '.' + cpf_encontrado[6:]
cpf_encontrado_formatado = cpf_encontrado_formatado[:11] + '-' + cpf_encontrado_formatado[11:]

if cpf_encontrado_formatado == cpf:
    print('O cpf encontrado é válido')
else:
    print('O cpf encontrado é inválido')    