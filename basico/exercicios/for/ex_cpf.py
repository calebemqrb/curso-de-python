cpf = '746.824.890-70'
# nmrs_do_cpf = []

# for nmr in cpf:
#     if nmr == '.' or nmr == '-':
#         continue
#     nmrs_do_cpf.append(int(nmr))

# nmrs_cpf_multiplicados = []
# contador = 10
# for i in range(0, 9):
#     nmrs_cpf_multiplicados.append(nmrs_do_cpf[i] * contador)
#     contador -= 1

# soma_nmrs_do_cpf_multiplicados = 0
# for nmr in nmrs_cpf_multiplicados:
#     soma_nmrs_do_cpf_multiplicados += nmr
# soma_nmrs_do_cpf_multiplicados = soma_nmrs_do_cpf_multiplicados * 10

# novo_nmr_gerado = soma_nmrs_do_cpf_multiplicados % 11
# novo_nmr_gerado = 0 if novo_nmr_gerado > 9  else novo_nmr_gerado


# Outra forma de resolução
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