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
print(novo_digito_gerado)