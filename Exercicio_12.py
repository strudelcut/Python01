#  Construa uma página/programa onde o usuário digitará dois números e o programa exibirá na tela, o menor dos números digitados.

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número para comparar com o anterior: "))

if (num1 < num2):
    print(f"O número {num1} é o menor")

elif(num2 < num1):
    print(f"O número {num2} é o menor")