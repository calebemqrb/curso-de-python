# Dava pra usar o enumerate
#Mas como não foi apresentado no curso ainda, não usei

lista = ['Maria','Helena', 'Luiz']

for i in range(len(lista)):
    print(i, lista[i])

#Resolução usando enumarate
for i, nome in enumerate(lista):
    print(i, nome)