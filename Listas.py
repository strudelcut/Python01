frutas = ['maça', 'banana', 'cereja']
#          [0]       [1]       [2]

frutas.append('melão')
frutas.append('abacaxi')
# frutas.pop(0)
frutas.sort()
frutas.reverse()
print(frutas)
# frutas.append(input('Digite uma fruta: '))

# print(len(frutas))
for i in range(len(frutas)):
    if frutas[i] == 'banana':
        frutas.pop(i)
        break

print(frutas)