# Comstrua uma página/programa onde o usuário digitará o nome e a média de dez aluno e o programa escreverá, na tela, o nome de todos com a média acima ou igual a seis.
# nomes = []
# medias = []
# nome = ""
# media = 0

# for i in range(10):
#     nome = input(f'Digite o {i+1}° nome de dez aluno: ')
#     media = float(input('Digite a média deste aluno: '))
#     if media >= 6 :
#         nomes.append(nome)
#         medias.append(media)

# for i in range(len(nomes)):
#     print(f"Nome: {nomes[i]}, média: {medias[i]}")

alunos = []
medias = []
def preencheListas():
    for i in range(10):
        alunos.append(input(f"Digite o nome do {i+1}° aluno: "))
        medias.append(float(input(f"Digite o média do {i+1}° aluno: ")))
    return
def retornaMariores():
    for i in range(10):
        if(medias[i] >= 6):
            print(f"aluno {alunos[i]} com média {medias[i]}")
    return
        
preencheListas()
retornaMariores()
