<<<<<<< HEAD
# Construa uma página/programa onde o usuário digitará o nome, o telefone e a cidade de dez pessoas. O programa exbirá, na tela, o nome e o telefone das pessoas que moram em Campo Grande.
=======
# Construa uma página/programa onde o usuário digitará o nome, o telefone e a cidade de dez pessoas. O programa exbirá, na tela, o nome e o telefone das pessoas que moram em 
# Campo Grande.

nomes = []
telefones = []
cidades = []

for i in range(10):
    nomes.append(input(f"Digite o {i+1}° nome de dez: "))
    telefones.append(input(f"Digite o {i+1}° telefone de dez: "))
    cidades.append(input(f"Digite a {i+1}ª cidade de dez: "))

nomes1 = []
telefones1 = []


for i in range(len(nomes)):
    if cidades[i] == "Campo Grande":
        nomes1.append(nomes[i])
        telefones1.append(telefones[i])

for i in range(len(nomes1)):
    print(f"Nome: {nomes1[i]}, Telefone: {telefones1[i]}")
>>>>>>> 9afa4cdbf03d88c8b2431ba59caea9643357c20a
