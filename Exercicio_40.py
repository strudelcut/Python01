# Construa uma página onde o usuário digitará o nome e a média de cinco alunos e o programa só aceitará a média do aluno caso ela esteja entre zero e dez.

def cadastrar():
    cadastro = []
    for i in range(5):
        nome = input(f"Digite o nome do {i+1}° aluno: ")
        media = int(input(f"Digite a média do {i+1}° aluno: "))
        if media > -1 and media <11:
            cadastro.append((nome, media))
    for cad in cadastro:
        print(f"Nome: {cad[0]}, Média: {cad[1]}.")
        
cadastrar()