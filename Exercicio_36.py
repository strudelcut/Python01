# Construa uma página/programa que o usuário digitará o nome e a idade de dez pessoas e o programa escreverá o nome do usuário mais novo
# nomes = []
# idade = []

# for i in range(10):
#     nomes.append(input(f"Digite o {i+1}° nome de dez: "))
#     idade.append(int(input("Digite a idade: ")))
    
# comparar = idade[0]
# menor = nomes[0]

# for j in range(len(idade)):
#     if(idade[j] < comparar):
#         comparar = idade[j]
#         menor = nomes[j]

# print(f'O usuário mais novo é: {menor}')
# print(nomes)
# print(idade)

# p1 = ["", 0]
# p2 = ["", 0]
# p3 = ["", 0]
# p1[0] = input("Digite o nome: ")
# p1[1] = int(input("Digite a idade: "))
# p2 = p1.copy()
# p3 = p1.copy()

# for i in range(4):
#     print(p3)
#     p1[0] = input("Digite o nome: ")
#     p1[1] = int(input("Digite a idade: "))
#     print(p3)
#     if(p1[1] <= p2[1]):
#         p3[0] = p1[0]
#         p3[1] = p1[1]
#     else:
#         p3[0] = p2[0]
#         p3[1] = p2[1]

# print(p3)

pessoa = []
for i in range(5):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    pessoa.append({"nome" : nome, "idade" : idade})
def buscar():
    i = 0
    menor = 0
    while(i<4):
        if(pessoa[i]["idade"] < pessoa[menor]["idade"]):
            menor = i
        else:
            menor=menor
        i += 1
    return menor
print(f"{pessoa[buscar()]}")