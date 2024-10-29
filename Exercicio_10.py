sal = float(input("Digite seu salário: "))
valorVT = sal * 0.06
valorPS = sal * 0.03

print(f"Valor do desconto do vale transporte: {valorVT}")
print(f"Valor do desconto do plano de saúde: {valorPS}")
print(f"O salário com os descontos do vale-transporte e plano de saúde é {sal - valorVT - valorPS}")