# Construa um programa onde o usuário digitará a sua idade. Se a idade for menor de 18 anos, o programa entrará em uma função listando nomes de programas infantis. 
# Caso seja maior de idade, entrará em uma outra função com lista de caoors e seus respectivos preços.

def ProgramasInfantis():
    lista1 = ['Pepa Pig', 'Chaves','Pantera cor de Rosa', 'Tom e Jerry']
    print(lista1)
    return

def Carros():
    # lista2 = ['Jeep Renegade - R$120.000', 'Amarok - R$350.000', 'HB20 - R$100.000', 'Mobi - R$70.000']
    carro = [{
        "Modelo" : "Jeep Renegade",
        "Preço" : 120000
    },
    {
        "Modelo" : "Amarok",
        "Preço" : 350000
    },
    {
        "Modelo" : "HB20",
        "Preço" : 100000
    },
    {
        "Modelo" : "Mobi",
        "Preço" : 70000
    }
    ]
    for c in carro:
        print(f"{c['Modelo']} Preço: R${c['Preço']}")
    return

idade = int(input("Digite sua idade: "))

if (idade >= 18):
    Carros()
else:
    ProgramasInfantis()

