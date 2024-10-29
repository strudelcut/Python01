# Construa uma página/programa onde o usuário digitará cinco números e o programa deverá colocar esses números dentro do vetor em ordem crescente.
vetor = []

for i in range(5):
    vetor.append(int(input(f'Digite o {i+1}° de cinco números: ')))
    vetor.sort()

print(vetor)