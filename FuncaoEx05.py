# Construa um programa/página onde o usuário irá digitar seu nome e cidade de onde está digitando. Essas informações passarão para uma função e, caso a cidade seja “Rio de Janeiro”, 
# a resposta, além do nome da pessoa, escreverá “Seja Bem-vindo à Cidade Maravilhosa”. Caso contrário, exibirá apenas o nome e a cidade digitada (utilizar passagem de parâmetros).

def saudacao(nome, cidade):
    if not cidade == "Rio de Janeiro":
        print(f"\nNome: {nome},\nCidade: {cidade}.\n")
    else:
        print(f"\n{nome}, seja bem-vindo à cidade maravilhosa.\n")
    return

nome = input("Digite um nome: ")
cidade = input("Digite um cidade: ")

saudacao(nome, cidade)