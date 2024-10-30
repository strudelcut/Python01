# Crie um jogo de par ou ímpar onde o computador irá gerar um número aleatório e o usuário irá digitar um número. Após digitar o número, o programa irá utilizar um vetor para
# resolver o jogo. Se a soma dos números for par, o usuário vence. Se for ímpar, o computador vence.

import random
def Game(numero):
    player2 = random.randint(0, 5)
    print(f"Player1: {numero}, Player2: {player2}")
    if (player2 + numero) % 2 == 0:
        return "PAR - Player1 venceu"
    else:
        return "ÍMPAR - Player2 venceu"

print("Jogo - Par ou Ímpar")
print("Números permitidos - 0, 1, 2, 3, 4 ou 5")
print()
print("-------------------------------------")
print()
jogadas = int(input("Quantas vezes deseja jogar: "))

for i in range(jogadas):
    player1 = int(input("Insira sua jogada: "))
    print(f"{Game(player1)}")
