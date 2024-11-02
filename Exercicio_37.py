# Construa uma página/programa onde o usuário digitará o nome, o telefone e a cidade de dez pessoas. O programa exbirá, na tela, o nome e o telefone das pessoas que moram em 
# Campo Grande.

# nomes = []
# telefones = []
# bairros = []

# for i in range(3):
#     nomes.append(input(f"Digite o {i+1}° nome de dez: "))
#     telefones.append(input(f"Digite o {i+1}° telefone de dez: "))
#     bairros.append(input(f"Digite a {i+1}ª cidade de dez: "))

# nomes1 = []
# telefones1 = []
# bairros1 = []


# for i in range(len(nomes)):
#     if bairros[i] == "Campo Grande":
#         nomes1.append(nomes[i])
#         telefones1.append(telefones[i])
#         bairros1.append(bairros[i])

# for i in range(len(nomes1)):
#     print(f"Nome: {nomes1[i]}, Telefone: {telefones1[i]}, Bairro: {bairros1[i]}.")

nomes = []
campo = []

for i in range(3):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    tel = input(f"Digite o telefone da {i+1}ª pessoa: ")
    bairro = input(f"Digite o bairro da {i+1}ª pessoa: ")
    nomes.append({'Nome': nome, 'Telefone': tel, 'Bairro': bairro})
    if bairro.lower() == 'campo grande':
        campo.append(nomes[i])

print(campo)
