# Construa uma página/programa onde o usuário digitará dois números, utilizando passagem de parâmetros e, dentro da função, irá calcular a soma desses dois números.

def soma(primeirapar, segundapar):
    print(f'Soma ou total: {primeirapar + segundapar}')
    return

par1 = int(input("Digite a primeira parcela da soma: "))
par2 = int(input("Digite a segunda parcela da soma: "))

soma(par1, par2)