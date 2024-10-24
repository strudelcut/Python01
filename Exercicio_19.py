# player1 = input("Jogador 1, escolha entre: papel, pedra ou tesoura: ")
# player2 = input("Jogador 2, escolha entre: papel, pedra ou tesoura: ")

# if(player1 == player2):
#     print("Empate")

# else:
#     if(player1 == "papel" and player2 == "pedra"):
#         print("Jogador 1 ganhou")
    
#     elif(player1 == "pedra" and player2 == "papel"):
#         print("Jogador 2 ganhou")
    
#     elif(player1 == "pedra" and player2 == "tesoura"):
#         print("Jogador 1 ganhou")
    
#     elif(player1 == "tesoura" and player2 == "pedra"):
#         print("Jogador 2 ganhou")
    
#     elif(player1 == "tesoura" and player2 == "papel"):
#         print("Jogador 1 ganhou")
    
#     elif(player1 == "papel" and player2 == "tesoura"):
#         print("Jogador 2 ganhou")
    
#     else:
#         print("Escolha inválida")


player1 = input("Jogador 1, escolha entre: papel, pedra ou tesoura: ")
player2 = input("Jogador 2, escolha entre: papel, pedra ou tesoura: ")

if(player1 == player2):
    print("Empate")

elif((player1 == "papel" and player2 == "pedra") or (player1 == "pedra" and player2 == "tesoura") or (player1 == "tesoura" and player2 == "papel")):
    print(f"Player 1 venceu!! ({player1} vence {player2})")
else:
    print(f"Player 2 venceu!! ({player2} vence {player1})")