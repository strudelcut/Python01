# Construa uma página/programa onde o usuário digitará seis números em um vetor e, depois esses números sejam exibidos na tela em ordem digitada.

num = []
for i in range(6):
    num.append(int(input(f'Digite o {i+1}° de seis números: ')))

i = 0
while len(num) > i:
    print(num[i])
    i += 1 
# for i in range(len(num)):
    # print(num[i])
print(num)