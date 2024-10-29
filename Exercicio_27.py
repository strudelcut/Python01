# Construa uma página/programa onde o usuário digitará um número, a página fará uma contagem regressiva até zero e, depois, contará de zero até o número que o usuário digitou.

num = int(input('Digite um número: '))

# for i in range(num, -1, -1):
#     print(i)

# for i in range(num):
#     print(i + 1)

num1 = 0
while num > 0:
    print(num)
    num -= 1
    num1 += 1

while num <= num1:
    print(num)
    num += 1