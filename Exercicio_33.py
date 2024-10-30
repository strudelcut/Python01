<<<<<<< HEAD
# Construa uma página/programa onde o usuário digitará sete números e o programa escreverá, na tela, quantos deles são pares e quantos são ímpares.

par = []
impar = []
num = 0

for i in range(7):
    num = int(input(f"Digite o {i+1}° de sete núemros: "))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

=======
# Construa uma página/programa onde o usuário digitará sete números e o programa escreverá, na tela, quantos deles são pares e quantos são ímpares.

par = []
impar = []
num = 0

for i in range(7):
    num = int(input(f"Digite o {i+1}° de sete núemros: "))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

>>>>>>> 9afa4cdbf03d88c8b2431ba59caea9643357c20a
print(f'Total de números pares: {len(par)}, são eles {par}.\n Total de números impares: {len(impar)}, são eles {impar}')