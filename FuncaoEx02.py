# Construa um programa/página onde o usuário digitará o seu nome e a saída dele será: "Seja Bem-vindo(a), Nome do usuário" com o nome do usuário (utilizar função).

def saudacao(nome):
    print(f"\nSeja Bem-vindo(a), {nome}.\n")
    return

nomeusuar = input("Digite um nome: ")

saudacao(nomeusuar)