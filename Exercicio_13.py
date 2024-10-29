#  Construa uma página/programa onde o usuário irá digitar sua idade e, caso a idade seja maior ou igual a 18, terá como resposta "Maior de Idade". Caso contrário, "Menoe de Idade".

idade = int(input("Digite a sua idade: "))

if(idade >= 18):
    print("Maior de Idade.")
else:
    print("Menor de Idade")