# Construa uma página/programa onde o usuário digitará oito números, o programa escreverá na tela qual deles é o maior e qual é o menor.

lista = []

for i in range(8):
    lista.append(int(input(f'Digite o {i+1}° de oito números: ')))

lista.sort()
print(f'O menor número: {lista[0]}. O maior número: {lista[len(lista)-1]}')
# lista.reverse()
# print(f'O maior número: {lista[0]}')