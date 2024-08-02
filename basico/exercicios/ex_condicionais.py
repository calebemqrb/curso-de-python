first_value = int(input("Insira o primeiro valor: "))
second_value = int(input("Insira o segundo valor: "))

if first_value > second_value:
    print(f'O primeiro valor({first_value}) é maior que o segundo({second_value})')
elif second_value > first_value:
    print(f'O segundo valor({second_value}) é maior que o primeiro({first_value})')
else:
    print(f'Os valores são iguais')