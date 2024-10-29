# Construa uma página onde o usuário digitará um valor e o programa mostrará, na tela, a tabuada de multiplicação deste número.

num = int(input('Digite o número que você queira saber a sua tabuada: '))

# for i in range(1, 11):
#     print(f'{num} X {i} = {num * i}')

i = 1
while i <= 10:
    print(f'{num} X {i} = {num * i}')
    i += 1