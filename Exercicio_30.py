# Construa uma página/programa onde o usuário digitará dez números e o programa somará e calculará a média dos números digitados.

num = []
soma = 0

for i in range(10):
    num.append(int(input(f'Digite {i+1}° de dez números: ')))

for i in range(len(num)):
    soma += num[i]

print(f'Soma: {soma}, Média: {soma / len(num)}')