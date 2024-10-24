# value = 3

# match value:
#     case 1:
#         Result = "One"
#     case 2:
#         Result = "Two"
#     case 3:
#         Result = "Three"
#     case _:
#         Result = "Default"

# print(Result)


total = 0
escolha = 0

while(escolha != 5):

    print("Cardápio:")
    print("1-Calabresa com Cebola - R$59,90\n2-Camarão com Catupiry - R$87,80\n3-Frango com Requeijão - R$65,50\n4-Banana com Chocolate - R$59,90")
    print("5 - Finalizar pedido")

    escolha = int(input("Digite a opção escolhida (apenas números): "))

    match escolha:
        case 1:
            print("Calabresa com Cebola - R$59,90")
            total += 59.9
        case 2:
            print("Camarão com Catupiry - R$87,80")
            total += 87.8
        case 3:
            print("Frango com Requeijão - R$65,50")
            total += 65.5
        case 4:
            print("Banana com Chocolate - R$59,90")
            total += 59.9
        case 5:
            print(f"Total do pedido: R${total}")
        case _:
            print("Escolha uma opção válida!")