# Construa uma página/programa que o usuário digitará um número e a aplicação completará o número digitado até completar cem.

num = int(input("Digite um número que será adicionado até cem: ")) + 1

while(num <= 100):
    print(num)
    num += 1


# for(num) in range(num, 101):
#     print(num)