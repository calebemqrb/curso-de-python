import random

nove_primeiros_digitos = ''
for digito in range(9):
    nove_primeiros_digitos += str(random.randint(0, 9))

contador = 10
soma_dos_digitos_multiplicados = 0
for digito in nove_primeiros_digitos:
    soma_dos_digitos_multiplicados += int(digito) * contador
    contador -= 1

soma_dos_digitos_multiplicados = soma_dos_digitos_multiplicados * 10
novo_digito_gerado = soma_dos_digitos_multiplicados % 11
novo_digito_gerado = 0 if novo_digito_gerado > 9 else novo_digito_gerado

dez_primeiros_digitos = nove_primeiros_digitos + str(novo_digito_gerado)
contador = 11
soma_dos_digitos_multiplicados = 0
for digito in dez_primeiros_digitos:
    soma_dos_digitos_multiplicados += int(digito) * contador
    contador -= 1

soma_dos_digitos_multiplicados = soma_dos_digitos_multiplicados * 10
novo_digito_gerado = soma_dos_digitos_multiplicados % 11
novo_digito_gerado = 0 if novo_digito_gerado > 9 else novo_digito_gerado
cpf_criado = dez_primeiros_digitos + str(novo_digito_gerado)

cpf_criado_formatado = cpf_criado[:3] + '.' + cpf_criado[3:]
cpf_criado_formatado = cpf_criado_formatado[:7] + '.' + cpf_criado[6:]
cpf_criado_formatado = cpf_criado_formatado[:11] + '-' + cpf_criado_formatado[11:]

print(cpf_criado_formatado)