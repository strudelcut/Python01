<<<<<<< HEAD
# Construa um programa/página onde o usuário digitará dez números. O programa deverá calcular quantos deles são maiores que dez.

list = []
maior = []

for i in range(10):
    list.append(int(input(f'Digite o {i+1}° de dez números: ')))

for i in range(len(list)):
    if list[i] > 10:
        maior.append(list[i])

print(f'Quantidade de números maiores que dez digitados foram: {len(maior)}, {maior}')
=======
# Construa um programa/página onde o usuário digitará dez números. O programa deverá calcular quantos deles são maiores que dez.

list = []
maior = []

for i in range(10):
    list.append(int(input(f'Digite o {i+1}° de dez números: ')))

for i in range(len(list)):
    if list[i] > 10:
        maior.append(list[i])

print(f'Quantidade de números maiores que dez digitados foram: {len(maior)}, {maior}')
>>>>>>> 9afa4cdbf03d88c8b2431ba59caea9643357c20a
