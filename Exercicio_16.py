# valor1 = int(input("Digite o primeiro número: "))
# valor2 = int(input("Digite segundo número: "))
# valor3 = int(input("Digite o terceiro número: "))

# #  Verificação se o valor1 é maior que o valor2
# if(valor1 > valor2):
#     # Caso verdadeiro, verifica se o valor1 é maior que valor3
#     if(valor1 > valor3):
#         print("O primeiro é maior!")
#     else:
#         print("O terceiro é maior!")
# # Caso valor1 seja menor, verificação se o valor2 é maior que valor3
# elif(valor2 > valor3):
#     print("O segundo é maior!")   
# else:
#     print("O terceiro é maior!")



# valor1 = int(input("Digite o primeiro número: "))
# valor2 = int(input("Digite segundo número: "))
# valor3 = int(input("Digite o terceiro número: "))

# if(valor1 == valor2 and valor1 == valor3):
#     print("Os 3 valores são iguais")
# elif(valor1 > valor2 and valor1 > valor3):
#     print("O primeiro é maior!")
# elif(valor2 > valor3):
#     print("O Segundo é o maior!")
# else:
#     print("O terceiro é maior!")



valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite segundo número: "))
valor3 = int(input("Digite o terceiro número: "))
valores = [valor1, valor2, valor3]

valores.sort()
valores.reverse()

print(valores[0])
