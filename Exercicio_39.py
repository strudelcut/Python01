# Construa uma página/programa onde o usuário digitará o nome e o bairro de dez pessoas. O programa exibirá o nome e bairro das pessoas em ordem alfabética.

# def get_people_info():
#     people = []
#     for i in range(3):
#         name = input(f'Digite o nome da pessoa {i+1}: ')
#         neighborhood = input(f'Digite o bairro da pessoa {i+1}: ')
#         people.append((name, neighborhood))
#     return people

# def print_sorted_people(people):
#     people.sort(key=lambda x: x[0])  # Ordena pelo nome
#     print("\nLista de Pessoas em Ordem Alfabética:")
#     for person in people:
#         print(f'Nome: {person[0]}, Bairro: {person[1]}')


# people = get_people_info()
# print_sorted_people(people)

pessoas = []

for i in range(3):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    bairro = input(f"Digite o bairro da {i+1}ª pessoa: ")
    pessoas.append((nome, bairro))

pessoas.sort(key = lambda n: n[0])

for pessoa in pessoas:
    print(f"Nome: {pessoa[0]}, Bairro: {pessoa[1]}.")