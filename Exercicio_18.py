nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

print(f"A média do aluno é: {media}")

if(media < 4):
    print("Aluno reprovado")
elif(media > 7):
    print("Aprovado direto")
else:
    print("Aluno em Recuperação")
    
    recuperação = float(input("Digite a nota de recuperação: "))
    
    if(recuperação < 5):
        print("Reprovado na recuperação")
    else:
        print("Aprovado na recuperação")