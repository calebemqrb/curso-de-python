nome = str(input("Digite seu nome: "))
altura = float(input("Digite sua altura: "))
peso = int(input("Digite seu peso: "))
imc = peso/ (altura **2)

print("Nome: ", nome)
print("Altura: ", altura)
print("Peso: ", peso)
print("IMC: ", imc)

# String formatada
print(f'{nome} tem {altura:.2f} de altura, pesa {peso}kg e seu IMC é de {imc}')