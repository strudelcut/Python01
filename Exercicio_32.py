# Construa um programa/página onde o usuário digitará dez números. O programa deverá calcular quantos deles são maiores que dez.

list = []
maior = []

for i in range(10):
    list.append(int(input(f'Digite o {i+1}° de dez números: ')))

for i in range(len(list)):
    if list[i] > 10:
        maior.append(list[i])

print(f'Quantidade de números maiores que dez digitados foram: {len(maior)}, {maior}')
