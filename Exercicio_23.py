# Construa uma página/programa onde o usuário digitará um número e o programa completará o número digitado até cem, apenas com números pares.

num = int(input("Digite um número que ele será adicionado até cem somente com números pares: "))

while(num <= 100):
    num += 1
    if(num % 2 == 0):
        print(num)


# for i in range(num, 101):
#     if(i % 2 == 0):
#         print(i)