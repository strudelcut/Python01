# Construa uma página/programa que o usuário digitará o nome e a idade de dez pessoas e o programa escreverá o nome do usuário mais novo
nomes = [""]
idade = []
comparar = 10000000000
menor = ''

for i in range(10):
    nomes.append(input(f"Digite o {i+1}° nome de dez: "))
    idade.append(int(input("Digite a idade: ")))
    
for j in range(len(idade)):
    if(idade[j] < comparar):
        comparar = idade[j]
        menor = nomes[j]

print(f'O usuário mais novo é: {menor}')
        